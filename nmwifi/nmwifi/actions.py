import time

from nmwifi.checks import (
    is_wifi_active,
    is_wifi_configured,
    is_ap_active,
    is_ap_configured,
)
from nmwifi.exceptions import (
    NotConfigured,
    WIFI_NOT_CONFIGURED,
    AP_NOT_CONFIGURED,
)


def activate_wifi(interface):
    if not is_wifi_configured(interface):
        raise WIFI_NOT_CONFIGURED

    if is_wifi_active(interface):
        # Wi-Fi is already active
        return

    # TODO activate wifi
    return


def activate_ap(interface):
    if not is_ap_configured(interface):
        raise AP_NOT_CONFIGURED

    if is_ap_active(interface):
        # Access Point is already active
        return

    # TODO activate ap
    return


def periodic_activate_wifi(interface, interval=600):
    while True:
        try:
            activate_wifi(interface)
        except NotConfigured:
            pass

        time.sleep(interval)


def remove_wifi(interface):
    if not is_wifi_configured(interface):
        return

    # TODO remove wifi
    pass


def remove_ap(interface):
    if not is_ap_configured(interface):
        return

    # TODO remove ap
    pass
