import time

from nmwifi import _nm_wrapper
from nmwifi.data import MIN_WIFI_STRENGTH
from nmwifi.checks import (
    verify_interface,
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


@verify_interface
def activate_wifi(interface):
    if not is_wifi_configured(interface):
        raise WIFI_NOT_CONFIGURED

    if is_wifi_active(interface):
        # Wi-Fi is already active
        return

    # TODO check if target SSID is in range
    # TODO activate wifi
    return


@verify_interface
def activate_ap(interface):
    if not is_ap_configured(interface):
        raise AP_NOT_CONFIGURED

    if is_ap_active(interface):
        # Access Point is already active
        return

    # TODO activate ap
    return


@verify_interface
def periodic_activate_wifi(interface, interval=300):
    while True:
        try:
            activate_wifi(interface)
        except NotConfigured:
            pass

        time.sleep(interval)


@verify_interface
def remove_wifi(interface):
    if not is_wifi_configured(interface):
        return

    # TODO remove wifi
    pass


@verify_interface
def remove_ap(interface):
    if not is_ap_configured(interface):
        return

    # TODO remove ap
    pass


@verify_interface
def available_networks(interface):
    networks = _nm_wrapper.list_available_networks(interface)
    networks = [
        (ssid, strength)
        for ssid, signal in networks
        if (strength := int(signal)) >= MIN_WIFI_STRENGTH
    ]
    networks.sort(key=lambda n: n[1], reverse=True)

    # filter duplicates
    unique_networks = []
    seen_ssids = set()
    for ssid, strength in networks:
        if ssid not in seen_ssids:
            unique_networks.append((ssid, strength))
            seen_ssids.add(ssid)

    return unique_networks
