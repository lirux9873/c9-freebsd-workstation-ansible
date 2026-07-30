from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    "ansible.cfg",
    "bootstrap.sh",
    "hosts",
    "local.yml",
    "requirements.yml",
    "group_vars/all.yml",
    "group_vars/workstations.yml",
    "group_vars/freebsd.yml",
    "host_vars/localhost.yml",
    "roles/base/tasks/main.yml",
    "roles/base/templates/FreeBSD.conf.j2",
    "roles/hardware/vars/virtualbox.yml",
    "roles/hardware/vars/dell_latitude_5591.yml",
    "roles/workstation/tasks/services.yml",
    "roles/desktop/tasks/sway.yml",
    "roles/desktop/tasks/dwm.yml",
    "roles/ansible_pull/templates/c9-ansible-pull.j2",
    "docs/host-changes.md",
]

missing = [item for item in required if not (ROOT / item).exists()]
if missing:
    raise SystemExit("Missing paths:\n- " + "\n- ".join(missing))

print("Project structure validation passed.")
