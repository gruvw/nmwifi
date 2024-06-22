from nmwifi import checks, data, exceptions, actions, _nm_wrapper


def setup(
    ap_ssid=None,
    ap_password=None,
    wifi_ssid=None,
    wifi_password=None,
    interface=None,
):
    setup_ap(ap_ssid, ap_password, interface)
    setup_wifi(wifi_ssid, wifi_password, interface)


def setup_wifi(wifi_ssid=None, wifi_password=None, interface=None):
    # set dummy wifi ssid + password if None
    actions.remove_wifi()

    # default connection details
    if wifi_ssid is None:
        if wifi_password is not None:
            raise exceptions.PASSWORD_WITHOUT_SSID

        wifi_ssid = data.UNEXISTING_WIFI_SSID
        wifi_password = data.UNEXISTING_WIFI_PASSWORD

    if not checks.is_valid_connection(wifi_ssid, wifi_password):
        raise exceptions.INVALID_CONNECTION_DETAILS

    _nm_wrapper.new_connection(
        data.CONNECTION_NAME_WIFI,
        wifi_ssid,
        wifi_password,
    )

    if interface:
        _nm_wrapper.activate_connection(interface, data.CONNECTION_NAME_WIFI)


def setup_ap(ssid_ap=None, password_ap=None, interface=None):
    # set default ap_ssid and no password if None
    actions.remove_ap()

    # default connection details
    if ssid_ap is None:
        if password_ap is not None:
            raise exceptions.PASSWORD_WITHOUT_SSID

        ssid_ap = data.default_ap_ssid(interface)

    if not checks.is_valid_connection(ssid_ap, password_ap):
        raise exceptions.INVALID_CONNECTION_DETAILS

    _nm_wrapper.new_connection(
        data.CONNECTION_NAME_AP,
        ssid_ap,
        password_ap,
    )

    if interface:
        _nm_wrapper.activate_connection(interface, data.CONNECTION_NAME_AP)


def clean():
    actions.remove_wifi()
    actions.remove_ap()
