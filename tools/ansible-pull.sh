#!/bin/sh

set -eu

REPOSITORY_URL="${REPOSITORY_URL:-https://github.com/lirux9873/c9-freebsd-workstation-ansible.git}"
REPOSITORY_BRANCH="${REPOSITORY_BRANCH:-main}"
WORK_DIRECTORY="${WORK_DIRECTORY:-/var/db/ansible-pull/c9-freebsd-workstation}"

if [ "$(uname -s)" != "FreeBSD" ]; then
    printf '%s\n' "ERROR: This command supports FreeBSD only." >&2
    exit 1
fi

exec /usr/local/bin/ansible-pull \
    --clean \
    --checkout "${REPOSITORY_BRANCH}" \
    --directory "${WORK_DIRECTORY}" \
    --inventory "${WORK_DIRECTORY}/hosts" \
    --url "${REPOSITORY_URL}" \
    local.yml \
    "$@"
