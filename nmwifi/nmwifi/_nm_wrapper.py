import re
import subprocess

from nmwifi import exceptions


SUDO = "sudo"
NMCLI = "nmcli"
DEFAULT_ARGS = ["-c", "no"]
ENCODING = "utf-8"


# Every function in this module supposes valid arguments.
# Invalid arguments crashing `nmcli` will raise a `CommandError`.


def _run(*args, as_sudo=False):
    cmd = [NMCLI, *DEFAULT_ARGS, *args]

    if as_sudo:
        cmd.insert(0, SUDO)

    complete = subprocess.run(cmd, capture_output=True)

    if complete.returncode != 0:
        error = complete.stderr.decode(ENCODING)
        raise exceptions.CommandError(" ".join(cmd) + "\n" + error)

    return complete.stdout.decode(ENCODING)


def _version():
    output = _run("--version")
    version_match = re.search(r"\d+.\d+.\d+", output)

    if not version_match:
        raise exceptions.CommandError(f"{NMCLI} version not found.")

    return version_match[0]


def _is_nm_available():
    try:
        version = _version()
        if version[0] != "1":
            return False
    except (FileNotFoundError, exceptions.CommandError):
        return False

    return True


def _findall(regex, content):
    return re.findall(regex, content, re.MULTILINE)


def wifi_interface_exists(interface):
    output = _run("-g", "device,type", "d")
    interfaces = _findall(r"^(.+):wifi$", output)

    return interface in interfaces


def get_mac_address(interface) -> str:
    output = _run("-t", "d", "show", interface)

    return _findall(r"^GENERAL.HWADDR:(.+)$", output)[0]


def list_available_networks(interface):
    output = _run("-g", "active,ssid,signal", "d", "wifi", "list", "ifname",
        interface)

    # ignore currently active ones
    return _findall(r"^no:(.+):(\d+)$", output)


def new_connection(name, ssid, password=None, ap_mode=False):
    add_args = ["c", "add", "type", "wifi", "con-name", name, "ssid", ssid,
        "autoconnect", "true", "connection.autoconnect-retries", "0",
        "connection.autoconnect-priority"]
    if ap_mode:
        add_args += ["9", "mode", "ap"]
    else:
        # Wi-Fi has higher priority (if not available start AP)
        add_args += ["10"]

    _run(add_args)

    if password:
        _run("c", "modify", name, "wifi-sec.key-mgmt", "wpa-psk",
            "wifi-sec.psk", password)

    if ap_mode:
        _run("c", "modify", name, "802-11-wireless.band", "bg", "ipv4.method",
            "shared", "ipv6.method", "disabled")


def activate_connection(interface, name):
    _run("c", "up", name, "ifname", interface)


def remove_connection(name):
    _run("c", "delete", name)


def connection_ssid(name):
    output = _run("-t", "c", "show", name)

    return _findall(r"^802-11-wireless.ssid:(.+)$", output)[0]


# verify NetworkManager available when importing
if not _is_nm_available():
    raise exceptions.NM_REQUIRED
