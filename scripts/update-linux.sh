#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/linux-common.sh"

usage() {
    cat <<'TEXT'
Usage: bash scripts/update-linux.sh [--pull] [--rebuild] [--import-syllabus]
  --pull             git pull --ff-only on the current branch; requires a clean checkout
  --rebuild          Rebuild bundled questions and tutorials from their authoring sources
  --import-syllabus  Import resources/German_telc_B1_complete_syllabus_after_A1.txt,
                    then rebuild questions and tutorials
Without options: validate current local edits, back up progress, and restart.
TEXT
}

pull=0
rebuild=0
import_syllabus=0
while (($#)); do
    case "$1" in
        --pull) pull=1 ;;
        --rebuild) rebuild=1 ;;
        --import-syllabus) import_syllabus=1; rebuild=1 ;;
        --help|-h) usage; exit 0 ;;
        *) usage >&2; die "Unknown option: $1" ;;
    esac
    shift
done
require_linux
installed_python
lock_maintenance
cd -- "$REPO_DIR"
if [[ "$pull" == 1 ]]; then
    command -v git >/dev/null || die 'git is required for --pull.'
    [[ -z "$(git status --porcelain)" ]] || die 'Commit or stash local changes before --pull, or omit --pull to deploy your local edits.'
    git pull --ff-only
fi
if [[ "$import_syllabus" == 1 ]]; then
    "$PYTHON" tools/import_syllabus.py
fi
if [[ "$rebuild" == 1 ]]; then
    "$PYTHON" tools/build_question_bank.py
    "$PYTHON" tools/build_tutorials.py
fi
validate_app
sudo -v
restart_service
printf '\nUpdate complete. Refresh the app in your browser to load the latest interface.\n'
