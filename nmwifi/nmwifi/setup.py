from typing import Optional

from . import checks, _data, exceptions, actions, _nm_wrapper


@_nm_wrapper.verify_interface
def setup(
    interface: str,
    wifi_ssid: Optional[str] = None,
    wifi_password: Optional[str] = None,
    ap_ssid: Optional[str] = None,
    ap_password: Optional[str] = None,
    activate: bool = True,
) -> None:
    """
    Sets up the Wi-Fi and Access Point (AP) connections configurations.
    This function can block for a few seconds when trying to connect to the
    Wi-Fi network (set activate to False to avoid).

    Args:
        interface (str): The name of the network interface to use.
        wifi_ssid (Optional[str]): The SSID of the Wi-Fi network.
        wifi_password (Optional[str]): The password for the Wi-Fi network.
        ap_ssid (Optional[str]): The SSID of the Access Point.
        ap_password (Optional[str]): The password for the Access Point.
        activate (bool, optional): Whether to activate the connections
            immediately. Default is True.

    Returns:
        None

    Raises:
        nmwifi.exceptions.InvalidConnectionParameters: If the SSID or password
            is invalid.
        nmwifi.exceptions.InvalidConnectionParameters: If a password is
            provided without an SSID.
    """

    setup_ap(interface, ap_ssid, ap_password, activate=activate)
    setup_wifi(interface, wifi_ssid, wifi_password, activate=activate)


@_nm_wrapper.verify_interface
def setup_wifi(
    interface: str,
    wifi_ssid: Optional[str] = None,
    wifi_password: Optional[str] = None,
    activate: bool = True,
) -> bool:
    """
    Sets up the Wi-Fi configuration.
    This function can block for a few seconds when trying to connect to the
    Wi-Fi network (set activate to False to avoid).

    Args:
        interface (str): The name of the network interface to use.
        wifi_ssid (Optional[str]): The SSID of the Wi-Fi network.
        wifi_password (Optional[str]): The password for the Wi-Fi network.
        activate (bool, optional): Whether to activate the connection
            immediately. Default is True.

    Returns:
        bool: True if the connection is activated, False otherwise.

    Raises:
        nmwifi.exceptions.InvalidConnectionParameters: If the SSID or password
            is invalid.
        nmwifi.exceptions.InvalidConnectionParameters: If a password is
            provided without an SSID.
    """

    actions.remove_wifi()

    # default connection details
    if wifi_ssid is None:
        if wifi_password is not None:
            raise exceptions.PASSWORD_WITHOUT_SSID

        # set dummy wifi ssid + password
        wifi_ssid = _data.UNEXISTING_WIFI_SSID
        wifi_password = _data.UNEXISTING_WIFI_PASSWORD

    if not checks.is_valid_connection(wifi_ssid, wifi_password):
        raise exceptions.INVALID_CONNECTION_DETAILS

    _nm_wrapper.new_connection(
        _data.CONNECTION_NAME_WIFI,
        wifi_ssid,
        wifi_password,
    )

    if activate:
        return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_WIFI)

    return False


@_nm_wrapper.verify_interface
def setup_ap(
    interface: str,
    ap_ssid: Optional[str] = None,
    ap_password: Optional[str] = None,
    activate: bool = True,
) -> bool:
    """
    Sets up the Access Point (AP) configuration.

    Args:
        interface (str): The name of the network interface to use.
        ap_ssid (Optional[str]): The SSID of the Access Point.
        ap_password (Optional[str]): The password for the Access Point.
        activate (bool, optional): Whether to activate the connection
            immediately. Default is True.

    Returns:
        bool: True if the connection is activated, False otherwise.

    Raises:
        nmwifi.exceptions.InvalidConnectionParameters: If the SSID or password
            is invalid.
    """

    actions.remove_ap()

    # default connection details
    if ap_ssid is None:
        ap_ssid = _data.default_ap_ssid(interface)

    if not checks.is_valid_connection(ap_ssid, ap_password):
        raise exceptions.INVALID_CONNECTION_DETAILS

    _nm_wrapper.new_connection(
        _data.CONNECTION_NAME_AP,
        ap_ssid,
        ap_password,
        ap_mode=True,
    )

    if activate:
        return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_AP)

    return False


def clean() -> None:
    """
    Removes both Wi-Fi and Access Point (AP) configurations.

    Returns:
        None
    """

    actions.remove_wifi()
    actions.remove_ap()
