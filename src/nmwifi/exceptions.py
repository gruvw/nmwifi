from click import ClickException


class NetworkManagerRequired(ClickException):
    """
    Exception raised when NetworkManager is required but not found.

    This exception indicates that the NetworkManager utility is not installed
    or not available on the system, and it is required for the `nmwifi`
    package to function properly.
    """
    pass


class InterfaceNotFound(ClickException):
    """
    Exception raised when the specified network interface is not found.

    This exception indicates that the given network interface name does not
    correspond to any network interface on the system.
    """
    pass


class NotConfigured(ClickException):
    """
    Exception raised when a requested operation is attempted on a
    non-configured entity.

    This exception is used when trying to activate or manipulate a Wi-Fi or
    Access Point configuration that has not been set up.
    """
    pass


class InvalidConnectionParameters(ClickException):
    """
    Exception raised when provided connection parameters are invalid.

    This exception indicates that the SSID or password provided for setting
    up a Wi-Fi or Access Point connection does not meet the required criteria
    (e.g., length requirements).
    """
    pass


class CommandError(ClickException):
    """
    Exception raised for generic command errors.

    This exception serves as a catch-all for various command execution errors
    that do not fit into the more specific exception categories.
    """
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
