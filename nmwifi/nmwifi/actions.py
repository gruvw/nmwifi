from . import _nm_wrapper, _data, checks, exceptions


@_nm_wrapper.verify_interface
def activate_wifi(interface):
    if not checks.is_wifi_configured():
        raise exceptions.WIFI_NOT_CONFIGURED

    if checks.is_wifi_active():
        # Wi-Fi is already active
        return True

    return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_WIFI)


@_nm_wrapper.verify_interface
def activate_ap(interface):
    if not checks.is_ap_configured():
        raise exceptions.AP_NOT_CONFIGURED

    if checks.is_ap_active():
        # Access Point is already active
        return True

    return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_AP)


def remove_wifi():
    if not checks.is_wifi_configured():
        return

    _nm_wrapper.remove_connection(_data.CONNECTION_NAME_WIFI)


def remove_ap():
    if not checks.is_ap_configured():
        return

    _nm_wrapper.remove_connection(_data.CONNECTION_NAME_AP)


@_nm_wrapper.verify_interface
def available_networks(interface):
    networks = _nm_wrapper.list_available_networks(interface)
    networks = [
        (ssid, strength)
        for ssid, signal in networks
        if (strength := int(signal)) >= _data.MIN_WIFI_STRENGTH
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
