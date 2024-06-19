from nmwifi import _nm_wrapper


# nmwifi NetworkManager connections
CONNECTION_WIFI = "nmwifi-wifi"
CONNECTION_AP = "nmwifi-ap"

# Dummy Wi-Fi credentials that should never exist
UNEXISTING_WIFI_SSID = "72b491ba-2230-4b01-9e98-a5b334f23c6f"
UNEXISTING_WIFI_PASSWORD = "52559422-5d46-437d-8920-2fef97d0cfe2"

# Default AP settings
DEFAULT_AP_SSID_PREFIX = "nmwifi"

# Connection details
MIN_SSID_LENGTH = 1
MIN_PASSWODR_LENGTH = 8

# Others
MIN_WIFI_STRENGTH = 15


def default_ap_ssid(interface):
    mac = _nm_wrapper.get_mac_address(interface)
    mac = mac.replace(":", "")
    suffix = mac[-4:]

    return f"{DEFAULT_AP_SSID_PREFIX}-{suffix}"
