#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/linux-common.sh"

usage() {
    cat <<'TEXT'
Usage: bash scripts/service-linux.sh COMMAND [argument]
  status              Show service status
  logs [--follow]     Show recent logs, optionally follow new entries
  start               Start and check the app
  stop                Stop until started manually or the machine reboots
  restart             Back up progress, restart, and check (no tests or content rebuild)
  backup              Create a consistent SQLite backup, even while the app runs
  restore FILE        Stop, back up current progress, restore FILE, and start
  disable             Stop and disable automatic startup; keep all files and progress
  enable              Enable automatic startup, start, and check
TEXT
}

command_name=${1:---help}
case "$command_name" in --help|-h) usage; exit 0 ;; esac
shift
case "$command_name" in
    logs) [[ $# == 0 || ( $# == 1 && "$1" == --follow ) ]] || die 'Use logs [--follow].' ;;
    restore) [[ $# == 1 ]] || die 'restore requires a backup file.' ;;
    status|start|stop|restart|backup|disable|enable) [[ $# == 0 ]] || die 'Unexpected argument.' ;;
    *) usage >&2; die "Unknown command: $command_name" ;;
esac
require_linux
installed_python
case "$command_name" in
    status) sudo systemctl status "$SERVICE" --no-pager ;;
    logs) sudo journalctl -u "$SERVICE" -n 100 --no-pager "$@" ;;
    *)
        lock_maintenance
        case "$command_name" in
            backup) "$PYTHON" "$HELPER" backup ;;
            restart) sudo -v; restart_service ;;
            start|enable)
                if [[ "$command_name" == enable ]]; then sudo systemctl enable "$SERVICE"; fi
                sudo systemctl reset-failed "$SERVICE"
                sudo systemctl start "$SERVICE"
                check_health ;;
            stop) sudo systemctl stop "$SERVICE" ;;
            disable) sudo systemctl disable --now "$SERVICE" ;;
            restore)
                "$PYTHON" "$HELPER" validate-db "$1"
                sudo -v
                RECOVER_SERVICE=1
                sudo systemctl stop "$SERVICE"
                "$PYTHON" "$HELPER" backup
                "$PYTHON" "$HELPER" restore "$1"
                sudo systemctl reset-failed "$SERVICE"
                sudo systemctl start "$SERVICE"
                RECOVER_SERVICE=0
                check_health ;;
        esac ;;
esac
