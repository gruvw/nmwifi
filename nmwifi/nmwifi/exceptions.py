class NetworkManagerRequired(Exception):
    pass


class InterfaceNotFound(Exception):
    pass


class NotConfigured(Exception):
    pass


class InvalidConnectionParameters(Exception):
    pass


class CommandError(Exception):
    pass


NM_REQUIRED = NetworkManagerRequired("NetworkManager utility is required.")

WIFI_NOT_CONFIGURED = NotConfigured("nmwifi Wi-Fi is not set up.")
AP_NOT_CONFIGURED = NotConfigured("nmwifi Access Point is not set up.")
AP_NOT_CONFIGURED = NotConfigured("nmwifi Access Point is not set up.")

INVALID_CONNECTION_DETAILS = InvalidConnectionParameters(
    "Invalid connection details: SSID or password."
)
PASSWORD_WITHOUT_SSID = InvalidConnectionParameters(
    "Provided a password without an SSID."
)
