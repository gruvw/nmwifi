from nmwifi.actions import remove_wifi, remove_ap
from nmwifi.checks import is_valid_connection
from nmwifi.data import (
    UNEXISTING_WIFI_SSID,
    UNEXISTING_WIFI_PASSWORD,
    default_ap_ssid
)
from nmwifi.exceptions import INVALID_CONNECTION_DETAILS, PASSWORD_WITHOUT_SSID


def setup(
    interface,
    ap_ssid=None,
    ap_password=None,
    wifi_ssid=None,
    wifi_password=None,
    activate=True,
):
    setup_ap(interface, ap_ssid, ap_password, activate=activate)
    setup_wifi(interface, wifi_ssid, wifi_password, activate=activate)


def setup_wifi(interface, wifi_ssid=None, wifi_password=None, activate=True):
    # set dummy wifi ssid + password if None
    remove_wifi(interface)

    # default connection details
    if wifi_ssid is None:
        if wifi_password is not None:
            raise PASSWORD_WITHOUT_SSID

        wifi_ssid = UNEXISTING_WIFI_SSID
        wifi_password = UNEXISTING_WIFI_PASSWORD

    if not is_valid_connection(wifi_ssid, wifi_password):
        raise INVALID_CONNECTION_DETAILS

    # TODO setup wifi
    pass


def setup_ap(interface, ap_ssid=None, ap_password=None, activate=True):
    # set default ap_ssid and no password if None
    remove_ap(interface)

    # default connection details
    if ap_ssid is None:
        if ap_password is not None:
            raise PASSWORD_WITHOUT_SSID

        ap_ssid = default_ap_ssid(interface)

    if not is_valid_connection(ap_ssid, ap_password):
        raise INVALID_CONNECTION_DETAILS

    # TODO setup ap
    pass
