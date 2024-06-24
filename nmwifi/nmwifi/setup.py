from . import checks, _data, exceptions, actions, _nm_wrapper


@_nm_wrapper.verify_interface
def setup(
    interface,
    ap_ssid=None,
    ap_password=None,
    wifi_ssid=None,
    wifi_password=None,
    activate=False,
):
    setup_ap(interface, ap_ssid, ap_password, activate=activate)
    setup_wifi(interface, wifi_ssid, wifi_password, activate=activate)


@_nm_wrapper.verify_interface
def setup_wifi(interface, wifi_ssid=None, wifi_password=None, activate=False):
    # set dummy wifi ssid + password if None
    actions.remove_wifi()

    # default connection details
    if wifi_ssid is None:
        if wifi_password is not None:
            raise exceptions.PASSWORD_WITHOUT_SSID

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
def setup_ap(interface, ssid_ap=None, password_ap=None, activate=False):
    # set default ap_ssid and no password if None
    actions.remove_ap()

    # default connection details
    if ssid_ap is None:
        ssid_ap = _data.default_ap_ssid(interface)

    if not checks.is_valid_connection(ssid_ap, password_ap):
        raise exceptions.INVALID_CONNECTION_DETAILS

    _nm_wrapper.new_connection(
        _data.CONNECTION_NAME_AP,
        ssid_ap,
        password_ap,
        ap_mode=True,
    )

    if activate:
        return _nm_wrapper.activate_connection(interface, _data.CONNECTION_NAME_AP)

    return False


def clean():
    actions.remove_wifi()
    actions.remove_ap()
