import functools

from nmwifi import _nm_wrapper
from nmwifi.data import MIN_PASSWODR_LENGTH, MIN_SSID_LENGTH
from nmwifi.exceptions import InterfaceNotFound

def is_valid_connection(ssid, password):
    # validate ssid
    if len(ssid) < MIN_SSID_LENGTH:
        return False

    if password is None:
        return True

    # validate password
    if len(password) < MIN_PASSWODR_LENGTH:
        return False

    return True


def verify_interface(func):
    @functools.wraps(func)
    def verify_interface_wrapper(interface, *args, **kwargs):
        if not _nm_wrapper.wifi_interface_exists(interface):
            raise InterfaceNotFound(interface)

        return func(interface, *args, **kwargs)
    return verify_interface_wrapper


@verify_interface
def is_wifi_active(interface):
    # do not check against which interface if None passed
    # if not configured return False
    # TODO
    pass


@verify_interface
def is_ap_active(interface):
    # TODO
    pass


def is_wifi_configured(interface):
    # TODO
    pass


def is_ap_configured(interface):
    # TODO
    pass
