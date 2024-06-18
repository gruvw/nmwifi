import re
import subprocess

from nmwifi.exceptions import CommandError, NM_REQUIRED, InterfaceNotFound


SUDO = "sudo"
NMCLI = "nmcli"
DEFAULT_ARGS = ["-c", "no"]
ENCODING = "utf-8"


def _run(*args, as_sudo=False):
    cmd = [NMCLI, *DEFAULT_ARGS, *args]

    if as_sudo:
        cmd.insert(0, SUDO)

    complete = subprocess.run(cmd, capture_output=True)

    if complete.returncode != 0:
        error = complete.stderr.decode(ENCODING)
        raise CommandError(" ".join(cmd) + "\n" + error)

    return complete.stdout.decode(ENCODING)


def _version():
    output = _run("--version")
    version_match = re.search(r"\d+.\d+.\d+", output)

    if not version_match:
        raise CommandError(f"{NMCLI} version not found.")

    return version_match[0]


def _is_nm_available():
    try:
        version = _version()
        if version[0] != "1":
            return False
    except (FileNotFoundError, CommandError):
        return False

    return True


def _findall(regex, content):
    return re.findall(regex, content, re.MULTILINE)


def wifi_interface_exists(interface):
    output = _run("-g", "device,type", "d")
    interfaces = _findall(r"^(.+):wifi$", output)

    return interface in interfaces


def _verify_interafce(interface):
    if not wifi_interface_exists(interface):
        raise InterfaceNotFound(interface)


def get_mac_address(interface) -> str:
    _verify_interafce(interface);

    output = _run("-t", "d", "show", interface)

    return _findall(r"^GENERAL.HWADDR:(.+)$", output)[0]


def list_available_networks(interface):
    _verify_interafce(interface);

    output = _run(
        "-g",
        "active,ssid,signal",
        "d",
        "wifi",
        "list",
        "ifname",
        interface
    )

    # ignore currently active ones
    return _findall(r"^no:(.+):(\d+)$", output)


# verify NetworkManager available when importing
if not _is_nm_available():
    raise NM_REQUIRED
