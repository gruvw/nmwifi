from . import _nm_wrapper, _data


def is_valid_connection(ssid, password):
    # validate ssid
    if len(ssid) < _data.MIN_SSID_LENGTH:
        return False

    if password is None:
        return True

    # validate password
    if len(password) < _data.MIN_PASSWODR_LENGTH:
        return False

    return True


def is_wifi_active():
    return _nm_wrapper.is_connection_active(_data.CONNECTION_NAME_WIFI)


def is_ap_active():
    return _nm_wrapper.is_connection_active(_data.CONNECTION_NAME_AP)


def is_wifi_configured():
    return _nm_wrapper.connection_exists(_data.CONNECTION_NAME_WIFI)


def is_ap_configured():
    return _nm_wrapper.connection_exists(_data.CONNECTION_NAME_AP)
