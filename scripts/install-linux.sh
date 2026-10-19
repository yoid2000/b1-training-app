#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/linux-common.sh"

usage() {
    cat <<'TEXT'
Usage: bash scripts/install-linux.sh [options]
  --install-prerequisites  Install python3, git, and util-linux using apt-get
  --host ADDRESS          Bind address (default: 0.0.0.0; keep existing on reinstall)
  --port NUMBER           TCP port, 1024–65535 (default: 8000; keep existing on reinstall)
  --import-db PATH        Import an existing app SQLite database on first installation
  --help                  Show this help
Run as your normal user. sudo is used for package and systemd setup only.
TEXT
}

host=''
port=''
import_db=''
prerequisites=0
while (($#)); do
    case "$1" in
        --install-prerequisites) prerequisites=1; shift ;;
        --host|--port|--import-db)
            (($# >= 2)) || die "$1 requires a value."
            case "$1" in
                --host) host=$2 ;;
                --port) port=$2 ;;
                --import-db) import_db=$2 ;;
            esac
            shift 2 ;;
        --help|-h) usage; exit 0 ;;
        *) usage >&2; die "Unknown option: $1" ;;
    esac
done

require_linux
sudo -v
if [[ "$prerequisites" == 1 ]]; then
    command -v apt-get >/dev/null || die '--install-prerequisites supports apt-get systems only; install Python 3.10+, git and util-linux with your distribution package manager.'
    sudo apt-get update
    sudo apt-get install -y python3 git util-linux
fi
require_python
lock_maintenance
if [[ -e "$UNIT_FILE" && ! -e "$CONFIG" ]]; then
    die "$UNIT_FILE already exists without our configuration; refusing to replace it."
fi

INSTALL_TMP="$(mktemp -d)"
"$PYTHON" "$HELPER" prepare --host "$host" --port "$port" --output "$INSTALL_TMP" --import-db "$import_db"
validate_app
# Validate the generated unit before installing it. This does not run the app.
systemd-analyze verify "$INSTALL_TMP/$SERVICE"

sudo install -d -m 0700 -o "$(id -u)" -g "$(id -g)" /var/lib/b1-training-app
if [[ -n "$import_db" ]]; then
    "$PYTHON" "$HELPER" import-db "$import_db"
fi
# Reinstallation preserves the database and existing host/port unless overridden.
sudo install -m 0644 -- "$INSTALL_TMP/config.json" "$CONFIG"
sudo install -m 0644 -- "$INSTALL_TMP/$SERVICE" "$UNIT_FILE"
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE"
restart_service
printf '\nInstalled. The app will start on reboot, without a user login.\n'
printf 'Guide: %s/docs/linux-installation.md\n' "$REPO_DIR"
