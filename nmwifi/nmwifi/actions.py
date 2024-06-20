import time

from nmwifi import _nm_wrapper, data, checks, exceptions


@checks.verify_interface
def activate_wifi(interface):
    if not checks.is_wifi_configured():
        raise exceptions.WIFI_NOT_CONFIGURED

    if checks.is_wifi_active(interface):
        # Wi-Fi is already active
        return

    # check if Wi-Fi ssid is in range
    target_ssid = _nm_wrapper.connection_ssid(data.CONNECTION_NAME_WIFI)
    networks = available_networks(interface)
    available_ssids = map(lambda n: n[0], networks)

    if target_ssid not in available_ssids:
        # Wi-Fi not available
        return

    _nm_wrapper.activate_connection(interface, data.CONNECTION_NAME_WIFI)


@checks.verify_interface
def activate_ap(interface):
    if not checks.is_ap_configured():
        raise exceptions.AP_NOT_CONFIGURED

    if checks.is_ap_active(interface):
        # Access Point is already active
        return

    _nm_wrapper.activate_connection(interface, data.CONNECTION_NAME_AP)


@checks.verify_interface
def periodic_activate_wifi(interface, interval=300):
    while True:
        try:
            activate_wifi(interface)
        except exceptions.NotConfigured:
            pass

        time.sleep(interval)


def remove_wifi():
    if not checks.is_wifi_configured():
        return

    _nm_wrapper.remove_connection(data.CONNECTION_NAME_WIFI)


def remove_ap():
    if not checks.is_ap_configured():
        return

    _nm_wrapper.remove_connection(data.CONNECTION_NAME_AP)


@checks.verify_interface
def available_networks(interface):
    networks = _nm_wrapper.list_available_networks(interface)
    networks = [
        (ssid, strength)
        for ssid, signal in networks
        if (strength := int(signal)) >= data.MIN_WIFI_STRENGTH
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
