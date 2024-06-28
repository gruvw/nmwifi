from typing import Optional

from . import _nm_wrapper, _data


def is_valid_connection(ssid: str, password: Optional[str]) -> bool:
    """
    Checks if the provided SSID and password combination is valid.

    Args:
        ssid (str): The SSID of the Wi-Fi network.
        password (Optional[str]): The password for the Wi-Fi network.

    Returns:
        bool: True if the connection details are valid, False otherwise.
    """

    # validate ssid
    if len(ssid) < _data.MIN_SSID_LENGTH:
        return False

    if password is None:
        return True

    # validate password
    if len(password) < _data.MIN_PASSWODR_LENGTH:
        return False

    return True


def is_wifi_active() -> bool:
    """
    Checks if the Wi-Fi connection is active.

    Returns:
        bool: True if the Wi-Fi is active, False otherwise.
    """

    return _nm_wrapper.is_connection_active(_data.CONNECTION_NAME_WIFI)


def is_ap_active() -> bool:
    """
    Checks if the Access Point (AP) connection is active.

    Returns:
        bool: True if the AP is active, False otherwise.
    """

    return _nm_wrapper.is_connection_active(_data.CONNECTION_NAME_AP)


def is_wifi_configured() -> bool:
    """
    Checks if the Wi-Fi connection is configured.

    Returns:
        bool: True if the Wi-Fi is configured, False otherwise.
    """

    return _nm_wrapper.connection_exists(_data.CONNECTION_NAME_WIFI)


def is_ap_configured() -> bool:
    """
    Checks if the Access Point (AP) connection is configured.

    Returns:
        bool: True if the AP is configured, False otherwise.
    """

    return _nm_wrapper.connection_exists(_data.CONNECTION_NAME_AP)
