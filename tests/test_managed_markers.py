from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

complete_templates = [
    "roles/base/templates/FreeBSD.conf.j2",
    "roles/base/templates/wheel-sudoers.j2",
    "roles/desktop/templates/sway-config.j2",
    "roles/desktop/templates/start-sway.j2",
    "roles/desktop/templates/waybar-config.jsonc.j2",
    "roles/desktop/templates/foot.ini.j2",
    "roles/desktop/templates/mako-config.j2",
    "roles/desktop/templates/xinitrc.j2",
    "roles/desktop/templates/picom.conf.j2",
    "roles/desktop/templates/dunstrc.j2",
    "roles/ansible_pull/templates/c9-ansible-pull.j2",
]

for relative in complete_templates:
    content = (ROOT / relative).read_text(encoding="utf-8")
    if "BEGIN ANSIBLE MANAGED FILE" not in content:
        raise SystemExit(f"{relative}: missing BEGIN marker")
    if "END ANSIBLE MANAGED FILE" not in content:
        raise SystemExit(f"{relative}: missing END marker")

for path in ROOT.rglob("tasks/*.yml"):
    content = path.read_text(encoding="utf-8")
    if "ansible.builtin.blockinfile" in content:
        if "ANSIBLE MANAGED BLOCK" not in content:
            raise SystemExit(
                f"{path.relative_to(ROOT)}: blockinfile lacks marker"
            )

print("Managed marker validation passed.")
