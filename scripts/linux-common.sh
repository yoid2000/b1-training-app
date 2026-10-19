#!/usr/bin/env bash
# Shared by the Linux entry points. Run those scripts, not this file.
set -euo pipefail

SERVICE=b1-training-app.service
CONFIG=/etc/b1-training-app.json
UNIT_FILE=/etc/systemd/system/b1-training-app.service
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
HELPER="$REPO_DIR/tools/linux_service.py"
RECOVER_SERVICE=0
INSTALL_TMP=''

die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

cleanup() {
    local result=$?
    if [[ "$RECOVER_SERVICE" == 1 ]]; then
        printf 'Attempting to start the service after an interrupted operation.\n' >&2
        sudo systemctl start "$SERVICE" || true
    fi
    if [[ -n "$INSTALL_TMP" ]]; then
        rm -f -- "$INSTALL_TMP/$SERVICE" "$INSTALL_TMP/config.json"
        rmdir -- "$INSTALL_TMP" || true
    fi
    exit "$result"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

require_linux() {
    [[ "$(uname -s)" == Linux ]] || die 'These scripts require Linux with systemd.'
    [[ "$EUID" != 0 ]] || die 'Run as your normal login user, without sudo before bash. The script uses sudo where needed.'
    command -v sudo >/dev/null || die 'sudo is required.'
    command -v systemctl >/dev/null || die 'systemctl is required.'
    [[ -d /run/systemd/system ]] || die 'systemd must be running as the system service manager.'
}

require_python() {
    command -v python3 >/dev/null || die 'Install Python 3.10+ first; on Debian/Ubuntu use the installer --install-prerequisites option.'
    PYTHON="$(python3 -c 'import sqlite3, sys; assert sys.version_info >= (3,10), "Python 3.10+ required"; print(sys.executable)')"
}

installed_python() {
    require_python
    # The helper checks that this checkout and user own the installed service.
    PYTHON="$("$PYTHON" "$HELPER" interpreter)"
}

lock_maintenance() {
    command -v flock >/dev/null || die 'flock is required (normally provided by util-linux).'
    mkdir -p -- "$REPO_DIR/instance"
    exec 9>"$REPO_DIR/instance/linux-maintenance.lock"
    flock -n 9 || die 'Another install, update, backup, or service operation is running.'
}

validate_app() {
    printf '\nChecking application and curriculum (includes 3,400 test answers)…\n'
    (cd -- "$REPO_DIR" && "$PYTHON" -m unittest discover -s tests -v)
}

check_health() {
    if ! "$PYTHON" "$HELPER" health; then
        sudo journalctl -u "$SERVICE" -n 40 --no-pager >&2 || true
        die 'Startup check failed. Inspect the logs; see docs/linux-installation.md for recovery.'
    fi
    sudo systemctl is-active "$SERVICE"
    printf 'Automatic startup: '
    sudo systemctl is-enabled "$SERVICE" || true
}

restart_service() {
    # Stop writes before taking the pre-restart snapshot. Recover on interruption.
    RECOVER_SERVICE=1
    sudo systemctl stop "$SERVICE"
    "$PYTHON" "$HELPER" backup --if-exists
    sudo systemctl reset-failed "$SERVICE"
    sudo systemctl start "$SERVICE"
    RECOVER_SERVICE=0
    check_health
}
