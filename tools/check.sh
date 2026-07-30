#!/bin/sh

set -eu

if [ "$(uname -s)" != "FreeBSD" ]; then
    printf '%s\n' "WARNING: Static checks are running outside FreeBSD." >&2
fi

/usr/local/bin/ansible-playbook -i hosts local.yml --syntax-check
/usr/local/bin/ansible-playbook -i hosts playbooks/validate.yml --syntax-check

printf '%s\n' "Ansible syntax checks passed."
