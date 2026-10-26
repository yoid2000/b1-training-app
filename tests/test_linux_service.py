"""Deployment helper checks, using temporary databases and no sudo/systemd calls."""

from contextlib import closing
import json
from pathlib import Path, PurePosixPath
import sqlite3
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

from app import QUESTION_BANK, Store, create_server
from tools import linux_service as service


class LinuxServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        self.database = self.folder / 'practice.sqlite3'
        self.data_patch = patch.multiple(service, DATA_DIR=self.folder, DATABASE=self.database,
                                         CONFIG=self.folder / 'service.json')
        self.data_patch.start()
        self.store = Store(self.database)
        with self.store.connect() as db:
            db.execute("INSERT INTO users(name) VALUES('Original learner')")

    def tearDown(self):
        self.data_patch.stop()
        self.temp.cleanup()

    def test_live_wal_backup_and_restore_preserve_profiles(self):
        # Keep a connection open so committed data still lives in SQLite's WAL.
        with self.store.connect() as writer:
            writer.execute("INSERT INTO users(name) VALUES('Committed in WAL')")
            writer.commit()
            learner = writer.execute('SELECT id, name FROM users WHERE id=1').fetchone()
            practice = self.store.start(writer, learner, {'unit_id': 1})
            writer.commit()
            question = QUESTION_BANK[1][0]
            self.store.answer(writer, learner, {'practice_id': practice['id'], 'question_id': question['id'],
                                               'choice': question['correct_index']})
            writer.commit()
            self.assertTrue(Path(str(self.database) + '-wal').exists())
            with patch('builtins.print'):
                snapshot = service.backup()
            self.assertTrue(snapshot.is_file())
            with closing(sqlite3.connect(snapshot)) as db:
                self.assertEqual(db.execute('SELECT name FROM users ORDER BY id').fetchall(),
                                 [('Original learner',), ('Committed in WAL',)])
                self.assertEqual(db.execute('SELECT COUNT(*) FROM answers').fetchone()[0], 1)
                self.assertEqual(db.execute('SELECT COUNT(*) FROM question_state').fetchone()[0], 1)
            writer.execute("UPDATE users SET name='Later change' WHERE id=1")
        service.copy_database(snapshot, self.database)
        with self.store.connect() as db:
            self.assertEqual([tuple(row) for row in db.execute('SELECT name FROM users ORDER BY id')],
                             [('Original learner',), ('Committed in WAL',)])
            self.assertEqual(self.store.dashboard(db, learner)['attempts'], 1)
        self.assertFalse(list(self.folder.glob('backups/*.partial')))

    def test_restore_rejects_missing_corrupt_and_foreign_databases(self):
        missing = self.folder / 'missing.sqlite3'
        bad = self.folder / 'not-sqlite.sqlite3'
        bad.write_text('This is not a database.', encoding='utf-8')
        foreign = self.folder / 'other.sqlite3'
        with closing(sqlite3.connect(foreign)) as db:
            db.execute('CREATE TABLE unrelated (id INTEGER)')
        for source in (missing, bad, foreign, self.database):
            with self.subTest(source=source), self.assertRaises((ValueError, sqlite3.Error)):
                service.copy_database(source, self.database)
        with self.store.connect() as db:
            self.assertEqual(db.execute('SELECT name FROM users').fetchone()[0], 'Original learner')
        self.assertFalse(missing.exists())

    def test_import_refuses_overwrite_and_cleans_up_failed_first_import(self):
        original = self.database.read_bytes()
        with self.assertRaises(ValueError):
            service.import_database(self.database)
        self.assertEqual(self.database.read_bytes(), original)
        destination = self.folder / 'first-install.sqlite3'
        with patch.object(service, 'DATABASE', destination):
            with self.assertRaises(ValueError):
                service.import_database(self.folder / 'missing.sqlite3')
            self.assertFalse(destination.exists())
            with patch('builtins.print'):
                service.import_database(self.database)
            service.validate_database(destination)

    def test_config_requires_original_checkout_and_user(self):
        config = {'format': 1, 'repo': str(service.ROOT), 'uid': 1000, 'python': sys.executable}
        service.CONFIG.write_text(json.dumps(config), encoding='utf-8')
        with patch.object(service.os, 'getuid', return_value=1000, create=True):
            self.assertEqual(service.load_config(), config)
        with patch.object(service.os, 'getuid', return_value=1001, create=True), self.assertRaises(ValueError):
            service.load_config()
        config['repo'] = '/some/other/checkout'
        service.CONFIG.write_text(json.dumps(config), encoding='utf-8')
        with patch.object(service.os, 'getuid', return_value=1000, create=True), self.assertRaises(ValueError):
            service.load_config()

    def test_prepare_preserves_settings_and_rejects_invalid_bind_options(self):
        old = {'host': '127.0.0.1', 'port': 8080}
        service.CONFIG.write_text('{}', encoding='utf-8')
        output = self.folder / 'generated'
        output.mkdir()
        with patch.object(service.os, 'getuid', return_value=1000, create=True), \
                patch.object(service.os, 'getgid', return_value=1000, create=True), \
                patch.object(service, 'load_config', return_value=old), \
                patch.object(service, 'DATA_DIR', self.folder / 'not-created-yet'), \
                patch.object(service, 'ROOT', PurePosixPath('/home/paul/app')), \
                patch.object(service.sys, 'executable', '/usr/bin/python3'), patch('builtins.print'):
            service.prepare('', '', output, '')
            config = json.loads((output / 'config.json').read_text(encoding='utf-8'))
            self.assertEqual((config['host'], config['port']), ('127.0.0.1', 8080))
            service.prepare('0.0.0.0', '9000', output, '')
            config = json.loads((output / 'config.json').read_text(encoding='utf-8'))
            self.assertEqual((config['host'], config['port']), ('0.0.0.0', 9000))
            for host, port in (('::1', '8188'), ('invalid', '8188'), ('0.0.0.0', '80'), ('0.0.0.0', '65536')):
                with self.subTest(host=host, port=port), self.assertRaises(ValueError):
                    service.prepare(host, port, output, '')
            with self.assertRaises(ValueError):
                service.prepare('', '', output, str(self.database))  # Existing progress is never overwritten.

    def test_unit_runs_unprivileged_with_persistent_state_and_boot_start(self):
        config = {'repo': '/home/paul/apps/b1-training-app', 'python': '/usr/bin/python3',
                  'uid': 1000, 'gid': 1001, 'host': '0.0.0.0', 'port': 8188}
        with patch.object(service, 'DATABASE', Path('/var/lib/b1-training-app/practice.sqlite3')):
            unit = service.render_unit(config)
        for setting in ('User=1000', 'Group=1001', 'WantedBy=multi-user.target', 'Restart=on-failure',
                        'StateDirectory=b1-training-app', 'ProtectHome=read-only', 'KillSignal=SIGINT',
                        '--database /var/lib/b1-training-app/practice.sqlite3'):
            self.assertIn(setting, unit)
        self.assertIn('WorkingDirectory=/home/paul/apps/b1-training-app', unit)
        self.assertNotIn('sudo', unit)
        self.assertEqual(service.safe_service_path('/srv/app-name_2.0'), '/srv/app-name_2.0')
        for path in ('/srv/app name', '/srv/%u', '/srv/$USER', '/srv/a\nExecStart=bad', 'relative', '/srv/../app'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                service.safe_service_path(path)

    def test_startup_health_check_uses_the_app_without_creating_profiles(self):
        server = create_server('127.0.0.1', 0, self.database)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            config = {'host': '0.0.0.0', 'port': server.server_port}
            with patch.object(service, 'load_config', return_value=config), patch('builtins.print'), patch('app.Handler.log_message'):
                service.health()
            with self.store.connect() as db:
                self.assertEqual(db.execute('SELECT COUNT(*) FROM users').fetchone()[0], 1)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == '__main__':
    unittest.main()
