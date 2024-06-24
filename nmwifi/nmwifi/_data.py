from . import _nm_wrapper


# nmwifi NetworkManager connections
CONNECTION_NAME_WIFI = "nmwifi-wifi"
CONNECTION_NAME_AP = "nmwifi-ap"

# Dummy Wi-Fi credentials that should never exist
UNEXISTING_WIFI_SSID = "72b491ba22304b019e98a5b334f23c6f"
UNEXISTING_WIFI_PASSWORD = "525594225d46437d89202fef97d0cfe2"

# AP settings
DEFAULT_AP_SSID_PREFIX = "nmwifi"

# Connection details
MIN_SSID_LENGTH = 1
MIN_PASSWODR_LENGTH = 8

# Others
MIN_WIFI_STRENGTH = 15


@_nm_wrapper.verify_interface
def default_ap_ssid(interface):
    mac = _nm_wrapper.get_mac_address(interface)
    mac = mac.replace(":", "")
    suffix = mac[-4:]

    return f"{DEFAULT_AP_SSID_PREFIX}-{suffix}"
