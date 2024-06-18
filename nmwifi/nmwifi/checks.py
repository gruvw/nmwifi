def is_valid_connection(ssid, password):
    # validate ssid
    if len(ssid) < MIN_SSID_LENGTH:
        return False

    if password is None:
        return True

    # validate password
    if len(password) < MIN_PASSWODR_LENGTH:
        return False

    return True


def is_wifi_active(interface=None):
    # do not check against which interface if None passed
    # if not configured return False
    # TODO
    pass


def is_ap_active(interface=None):
    # TODO
    pass


def is_wifi_configured(interface=None):
    # TODO
    pass


def is_ap_configured(interface=None):
    # TODO
    pass
