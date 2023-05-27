import subprocess

def get_tag_or_branch():
    return subprocess.run(
        "git describe --exact-match --tags HEAD 2>/dev/null || git rev-parse --abbrev-ref HEAD",
        shell=True,
        capture_output=True
    ).stdout.decode().strip()

def get_revision():
    return subprocess.run(
        "git rev-parse --short=10 HEAD",
        shell=True,
        capture_output=True
    ).stdout.decode().strip()

def get_dirty():
    return subprocess.run(
        '[ -z "$(git status --porcelain)" ] && echo "clean" || echo "dirty"',
        shell=True,
        capture_output=True
    ).stdout.decode().strip()
