from typing import List, Tuple

from . import _nm_wrapper, _data, checks, exceptions


@_nm_wrapper.verify_interface
def activate_wifi(interface: str) -> bool:
    """
    Activates the Wi-Fi connection on the specified network interface.
    Does nothing if the Wi-Fi is already active.

    Args:
        interface (str): The name of the network interface to use.

    Returns:
        bool: True if the Wi-Fi was already active, False otherwise.

    Raises:
        nmwifi.exceptions.NotConfigured: If the Wi-Fi is not configured.
    """

    if not checks.is_wifi_configured():
        raise exceptions.WIFI_NOT_CONFIGURED

    if checks.is_wifi_active():
        # Wi-Fi is already active
        return True

    return _nm_wrapper.activate_connection(
        interface,
        _data.CONNECTION_NAME_WIFI
    )


@_nm_wrapper.verify_interface
def activate_ap(interface: str) -> bool:
    """
    Activates the Access Point (AP) on the specified network interface.
    Does nothing if the AP is already active.

    Args:
        interface (str): The name of the network interface to use.

    Returns:
        bool: True if the AP was already active, False otherwise.

    Raises:
        nmwifi.exceptions.NotConfigured: If the AP is not configured.
    """

    if not checks.is_ap_configured():
        raise exceptions.AP_NOT_CONFIGURED

    if checks.is_ap_active():
        # Access Point is already active
        return True

    return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_AP)


def remove_wifi() -> None:
    """
    Removes the Wi-Fi connection configuration.
    Does nothing if Wi-Fi is not configured.

    Returns:
        None
    """

    if not checks.is_wifi_configured():
        return

    _nm_wrapper.remove_connection(_data.CONNECTION_NAME_WIFI)


def remove_ap() -> None:
    """
    Removes the Access Point (AP) configuration.
    Does nothing if AP is not configured.

    Returns:
        None
    """

    if not checks.is_ap_configured():
        return

    _nm_wrapper.remove_connection(_data.CONNECTION_NAME_AP)


@_nm_wrapper.verify_interface
def available_networks(interface: str) -> List[Tuple[str, int]]:
    """
    Lists available Wi-Fi networks with signal strength.
    The list is sorted by descending signal strength.
    Each SSID appears only once.

    Args:
        interface (str): The name of the network interface to use.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing SSID and signal
            strength.
    """

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
