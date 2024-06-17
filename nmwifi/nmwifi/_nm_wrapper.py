import re
import subprocess

from nmwifi.exceptions import CommandError, NM_REQUIRED


NMCLI = "nmcli"
SUDO = "sudo"
ENCODING = "utf-8"


def _run(args, as_sudo=False):
    cmd = [NMCLI, args]

    if as_sudo:
        cmd.insert(0, SUDO)

    complete = subprocess.run(cmd, capture_output=True)

    if complete.returncode != 0:
        raise CommandError(" ".join(cmd))

    return complete.stdout.decode(ENCODING)


def _version():
    output = _run("--version")
    version_match = re.search(r"\d+.\d+.\d+", output)

    if not version_match:
        raise CommandError(f"{NMCLI} version not found.")

    return version_match[0]


def _verify_nm():
    try:
        version = _version()
        if version[0] != "1":
            return False
    except (FileNotFoundError, CommandError):
        return False

    return True


def interface_exists(interface):
    # TODO
    pass


def get_mac_address(interface) -> str:
    # TODO
    pass


# verify NetworkManager available when importing
if not _verify_nm():
    raise NM_REQUIRED
