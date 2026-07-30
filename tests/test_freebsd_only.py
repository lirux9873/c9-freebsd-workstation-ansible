from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

forbidden_patterns = {
    "apt module or command": r"\bapt(?:-get)?\b",
    "dnf module or command": r"\bdnf\b",
    "yum module or command": r"\byum\b",
    "pacman module or command": r"\bpacman\b",
    "systemctl": r"\bsystemctl\b",
    "systemd path": r"/(?:usr/)?lib/systemd",
    "Linux default configuration path": r"/etc/default/",
}

excluded = {
    Path("tests/test_freebsd_only.py"),
    Path("README.md"),
    Path("docs/architecture.md"),
}

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    relative = path.relative_to(ROOT)
    if relative in excluded or ".git" in relative.parts:
        continue

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    import re
    for description, pattern in forbidden_patterns.items():
        if re.search(pattern, content, flags=re.IGNORECASE):
            raise SystemExit(
                f"{relative}: contains forbidden Linux-specific "
                f"{description}"
            )

print("FreeBSD-only validation passed.")
