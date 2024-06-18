from nmwifi._nm_wrapper import get_mac_address


# Dummy Wi-Fi credentials that should never exist
UNEXISTING_WIFI_SSID = "72b491ba-2230-4b01-9e98-a5b334f23c6f"
UNEXISTING_WIFI_PASSWORD = "52559422-5d46-437d-8920-2fef97d0cfe2"

# Default AP settings
DEFAULT_AP_SSID_PREFIX = "NMWiFi"

# Others
MIN_WIFI_STRENGTH = 15


def default_ap_ssid(interface):
    mac = get_mac_address(interface)
    mac.replace(":", "")

    suffix = mac[-4:]

    return f"{DEFAULT_AP_SSID_PREFIX}-{suffix}"
