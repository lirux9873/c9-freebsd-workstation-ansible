#!/bin/sh

set -eu

REPOSITORY_URL="${REPOSITORY_URL:-https://github.com/lirux9873/c9-freebsd-workstation-ansible.git}"
REPOSITORY_BRANCH="${REPOSITORY_BRANCH:-main}"
WORK_DIRECTORY="${WORK_DIRECTORY:-/var/db/ansible-pull/c9-freebsd-workstation}"

if [ "$(uname -s)" != "FreeBSD" ]; then
    printf '%s\n' "ERROR: This bootstrap supports FreeBSD only." >&2
    exit 1
fi

if [ "$(id -u)" -ne 0 ]; then
    printf '%s\n' "ERROR: Run bootstrap.sh as root." >&2
    exit 1
fi

env ASSUME_ALWAYS_YES=yes pkg bootstrap -f
pkg install -y ca_root_nss git sysutils/py-ansible-core sudo

install -d -o root -g wheel -m 0755 "${WORK_DIRECTORY}"

exec /usr/local/bin/ansible-pull \
    --clean \
    --checkout "${REPOSITORY_BRANCH}" \
    --directory "${WORK_DIRECTORY}" \
    --inventory "${WORK_DIRECTORY}/hosts" \
    --url "${REPOSITORY_URL}" \
    local.yml
