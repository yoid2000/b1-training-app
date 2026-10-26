# Install and maintain Schritt on Linux

Run the scripts **as your normal login user**. Do not put `sudo` before `bash`; the scripts request it for package installation and systemd operations. The app itself runs as your user, with no root privileges.

The installation uses a **system systemd service**, so the app starts after a reboot **without anyone logging in**. Repository changes are deployed with one update script. Learner profiles, sessions, answers, and progress are stored outside the repository.

## Requirements and layout

Use a Linux distribution with **systemd**, **Bash**, **Python 3.10 or newer with SQLite support**, `sudo`, and `flock` (normally part of `util-linux`). Git is needed if you clone or pull the repository. Debian, Ubuntu, and Raspberry Pi OS installations using systemd fit this approach when their Python version meets the requirement. There are no pip packages or virtual environments to install.

The optional prerequisite installer uses `apt-get`. On other distributions, install these packages with the distribution's package manager before running the app installer.

| Item | Location |
| --- | --- |
| Code and bundled learning content | Your checkout, for example `/home/paul/apps/b1-training-app` |
| Learner database used by the service | `/var/lib/b1-training-app/practice.sqlite3` |
| Database snapshots | `/var/lib/b1-training-app/backups/` |
| Service definition | `/etc/systemd/system/b1-training-app.service` |
| Installation settings | `/etc/b1-training-app.json` |
| App logs | systemd journal; use the logs script below |

Keep the checkout in a permanent location accessible at boot. The checkout and Python paths must contain only ASCII letters, digits, `/`, `.`, `_`, `@`, `+`, or `-`, with **no spaces**. The scripts reject other paths rather than generating an ambiguous service definition. Do not move the checkout or switch installation accounts after installation; the maintenance scripts check both.

If your home directory is unlocked only when you log in, put the checkout on a boot-accessible filesystem instead. For example, create an ordinary user-owned directory once, then clone into it:

```bash
sudo install -d -m 0755 -o "$(id -u)" -g "$(id -g)" /srv/b1-training-app
git clone https://github.com/yoid2000/b1-training-app.git /srv/b1-training-app
cd /srv/b1-training-app
```

The remaining examples assume commands are run from the checkout. The scripts also work when invoked by their absolute paths from another directory. They are invoked with `bash`, so no `chmod` step is needed.

## First installation

If you already copied or cloned the repository to Linux, enter that directory and skip the clone. Otherwise, with Git installed:

```bash
mkdir -p "$HOME/apps"
git clone https://github.com/yoid2000/b1-training-app.git "$HOME/apps/b1-training-app"
cd "$HOME/apps/b1-training-app"
```

If Git is missing on a Debian/Ubuntu-based machine, the one bootstrap command needed before cloning is `sudo apt-get update && sudo apt-get install -y git`. Network access is needed for cloning and package installation; running the app needs none.

Install and start the app:

```bash
bash scripts/install-linux.sh --install-prerequisites
```

Omit `--install-prerequisites` when Python, Git, and `util-linux` are already installed, or when using a distribution without `apt-get`:

```bash
bash scripts/install-linux.sh
```

The installer checks the configuration, runs the Python test suite using temporary databases, validates the service definition, installs and enables the service, and checks the app's HTTP response. The tests currently exercise all 3,400 answers and can take a minute or more. A failed check stops installation with a nonzero exit status.

For a **new service installation**, the default bind address is `0.0.0.0`, port **8188**, allowing connections from other WLAN devices. To choose another port:

```bash
bash scripts/install-linux.sh --port 8080
```

Ports must be between 1024 and 65535. To restrict access to the Linux device itself, use `--host 127.0.0.1`. A specific IPv4 bind address is also supported; it must be assigned to the machine. Binding to `0.0.0.0` is usually easier with DHCP. The app currently serves IPv4.

The installer can be run again to repair the service or change the host/port. It keeps the existing host and port when those options are omitted and preserves the service database. It refuses to replace a service belonging to another checkout or account. When a future repository update changes the service definition or installation settings, re-run this installer; the regular update script does not rewrite systemd configuration.

### Change an existing installation to port 8188

An older installation may have port **8000** saved in `/etc/b1-training-app.json`. Running `bash scripts/install-linux.sh` again without `--port` preserves that saved port, even though the current default is 8188. In that case, output such as `Listen: 0.0.0.0:8000` reflects the saved configuration.

To switch the existing service to 8188, run:

```bash
bash scripts/install-linux.sh --port 8188
```

This saves the new port and restarts the service, preserving learner progress. With the default bind address, the installer should print `Listen: 0.0.0.0:8188`. Open the app using port 8188 and update any firewall rule that previously allowed port 8000. Later installer runs without `--port` will keep 8188.

## Preserve progress from an existing manual installation

Stop any manually started copy of `python3 app.py` before switching to the service. It may already be using port 8188. For a first service installation with existing progress:

```bash
bash scripts/install-linux.sh --import-db instance/practice.sqlite3
```

You can combine this with `--install-prerequisites` or `--port`. The original database is retained. The import uses SQLite's backup API, which includes committed data in the WAL; it does not copy only the main database file. The installer refuses to overwrite an existing service database. If it finds a manual-run database but you did not request an import, it stops with instructions rather than silently starting with empty progress.

For progress from another machine, create a backup there using the backup script below, transfer the resulting snapshot to Linux, and pass its path to `--import-db`. To replace progress after the service is installed, use the explicit restore command below.

Once installed, use the service scripts. A plain `python3 app.py` still uses the checkout's `instance/practice.sqlite3` by default, which is a different database from the service's database.

## Open the app and check reboot startup

On the Linux machine open **http://localhost:8188**. On another WLAN device open **http://LINUX-IP:8188**, using your chosen port if different. Find the address with:

```bash
hostname -I
```

Use the WLAN IPv4 address, not a Docker/VPN address. A DHCP reservation in your router can keep the address stable. The Linux machine must be awake; reboot startup does not prevent system sleep.

If a firewall is enabled, allow the chosen TCP port **from your trusted WLAN subnet**. The scripts do not change firewall rules. For example, **only if your subnet is actually `192.168.1.0/24` and you use UFW**:

```bash
sudo ufw allow from 192.168.1.0/24 to any port 8188 proto tcp
```

Do not enable a new firewall remotely without preserving your SSH access. Profiles have no passwords, so keep this service on the trusted network and do not forward its port from the internet.

Check status:

```bash
bash scripts/service-linux.sh status
```

The output should show `enabled` and `active (running)`. To verify the real boot path, reboot once when convenient:

```bash
sudo reboot
```

After the machine rejoins the WLAN, open the app from another device **before logging into Linux**. Then log in and check status if needed. This confirms the checkout, interpreter, filesystem, and network are available during boot.

## Deploy code or curriculum changes

The scripts operate on the checkout used during installation. They do not discard edits, switch branches, force Git updates, or automatically deploy future commits on boot. A reboot starts whatever version is already in that checkout.

### Changes made directly on the Linux device

Edit the code or bundled content, then run:

```bash
bash scripts/update-linux.sh
```

To edit the question or tutorial **authoring sources** and regenerate the bundled JSON as part of deployment:

```bash
bash scripts/update-linux.sh --rebuild
```

This rebuilds both `data/questions_021_170.json` and `data/tutorials.json`. Questions for units 1–20 are authored directly in `content.py`; no question rebuild is needed for those edits. See [the curriculum instructions](../README.md#add-or-revise-curriculum) for source formats.

For changes to the original syllabus text and bundled metadata:

```bash
bash scripts/update-linux.sh --import-syllabus
```

This imports the syllabus and rebuilds both content bundles. It requires the ignored file `resources/German_telc_B1_complete_syllabus_after_A1.txt` to be present on this machine. Ordinary updates and installation do not require `resources/`.

### Changes committed on another computer

Commit and push the code, authoring sources, and rebuilt JSON on the development computer. On Linux:

```bash
bash scripts/update-linux.sh --pull
```

The script runs `git pull --ff-only` using the current branch's configured upstream. It requires a clean checkout, including untracked files. Commit or stash local edits first, or omit `--pull` to deploy those local edits. It never resolves merges automatically. Git authentication, if required, uses your normal user account.

If a pulled change intentionally includes authoring-source edits without rebuilt JSON, use `--pull --rebuild`; commit the generated files afterward. Normally commit the generated JSON on the development computer so the Linux checkout stays clean.

### What an update does

1. Optionally pulls commits and/or regenerates bundled content.
2. Runs the Python checks against temporary databases, while the existing service continues running.
3. Stops the service briefly, takes a consistent backup of learner progress, and starts the service again.
4. Checks the local HTTP response and reports service and automatic-startup status.

If rebuilding or tests fail, the script does not stop or restart the service. It leaves your source edits and generated files available to fix; it does not undo them. Because the service uses this checkout directly, static-file edits can be visible before a restart. For larger changes, develop and test elsewhere, then pull during a quiet period.

After a successful update, refresh open browser tabs to load the new interface. In-progress learning attempts remain in the database.

Keep question IDs, meanings, and option ordering stable once learners have answered them: saved answers refer to a question ID and option index. Improving an explanation is straightforward. Replacing a question's meaning or reordering its choices needs a deliberate data migration or new question ID. The current builders, UI, and tests target 170 units with 20 questions each; expanding those counts also requires updating the corresponding code and checks.

## Everyday service commands

```bash
bash scripts/service-linux.sh status
bash scripts/service-linux.sh logs
bash scripts/service-linux.sh logs --follow
bash scripts/service-linux.sh restart
bash scripts/service-linux.sh stop
bash scripts/service-linux.sh start
```

`restart` backs up progress and checks startup, but skips tests and content rebuilding. Use `update-linux.sh` for the normal validate-and-deploy workflow. `stop` leaves boot startup enabled, so the next reboot starts the app again. Press **Ctrl+C** to leave followed logs; this does not stop the app. `status` returns a nonzero exit status if the service is stopped or failed.

To stop it and prevent automatic startup, while retaining all files and progress:

```bash
bash scripts/service-linux.sh disable
```

To enable boot startup and start again:

```bash
bash scripts/service-linux.sh enable
```

## Back up and restore learner progress

Create a consistent snapshot, including while learners are using the app:

```bash
bash scripts/service-linux.sh backup
```

The script prints the snapshot's exact path under `/var/lib/b1-training-app/backups/`. Backups contain all profiles, session selections, attempts, and answers as of the snapshot. They are created with private file permissions. Automatic snapshots are also taken before updates, restarts, reinstalls with an existing database, and restores. No snapshots are deleted automatically; monitor disk space and remove old ones deliberately after keeping the copies you need.

Copy important snapshots to another machine or disk. Backups beside the live database do not protect against failure of that disk. They contain **learner data only**; retain the matching repository revision and installation settings separately. No SQLite command-line package is required.

To restore a snapshot, replacing **all** current learner data:

```bash
bash scripts/service-linux.sh restore /path/to/practice-SNAPSHOT.sqlite3
```

The script validates the snapshot, stops the app, backs up the current data, restores using SQLite, and starts/checks the app. Learners lose changes made after the restored snapshot. Do not replace a live database with `cp` or copy its main file while ignoring `-wal`/`-shm`; use these scripts. Refresh browser tabs after a restore; a newer browser session may require selecting a profile again.

## Troubleshooting and recovery

Start with:

```bash
bash scripts/service-linux.sh status
bash scripts/service-linux.sh logs
```

| Symptom | Action |
| --- | --- |
| `Address already in use` | Stop a manually started app or another service using the port, or re-run the installer with a different `--port`. |
| Works locally but not from WLAN | Check the WLAN IP, chosen port, firewall subnet rule, and whether the router isolates wireless clients. Check that you did not install with `--host 127.0.0.1`. |
| Works after login, fails at boot | Ensure the checkout and Python installation are accessible before login; a login-unlocked home directory is unsuitable. Check the journal after boot. |
| Test or rebuild failure | Fix the reported source/content issue, then run the update again. The update has not restarted the service at this point. |
| Startup check fails after restart | Read the printed journal output. Fix the code, port, or permissions and rerun the update. There is no automatic code rollback. |
| Python version too old | Install Python 3.10+ using your distribution's supported packages, then rerun installation. The prerequisite option does not add third-party repositories or upgrade the OS. |
| Wrong checkout/account message | Run the scripts from the original installed checkout as its original user. Installation details are in `/etc/b1-training-app.json`. |
| A maintenance operation is already running | Wait for it to finish. The kernel releases the lock when that process exits; deleting the lock file is unnecessary. |

For a bad deployed commit, fix it or revert it in Git, then run `update-linux.sh` again. A code rollback normally does **not** require restoring learner data. If you intentionally need the earlier data too, use the restore command with the pre-update snapshot. Fix local edits before using `--pull`; the script will not erase them.

Re-run `install-linux.sh` to refresh the service definition while keeping the service database. Before moving a deployment to a new machine, take an off-device backup, clone the code there, and use `--import-db` on the new installation.

The implementation follows the upstream [systemd service documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html), [systemctl enable/start behavior](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html), and [persistent state-directory handling](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#RuntimeDirectory=). The scripts validate the generated unit and check real HTTP startup during installation; an actual reboot check must be performed on the target Linux machine.
