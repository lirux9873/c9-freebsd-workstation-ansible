from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

tests = [
    "test_structure.py",
    "test_freebsd_only.py",
    "test_managed_markers.py",
]

for test in tests:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tests" / test)],
        cwd=ROOT,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)

print("All static tests passed.")
