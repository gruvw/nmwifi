import time
from typing import NoReturn

from . import _nm_wrapper, actions, exceptions


@_nm_wrapper.verify_interface
def balance(interface: str, interval: int = 900) -> NoReturn:
    """
    Periodically tries to maintain a connection to the configured Wi-Fi
    network while on Access Point mode.
    Does nothing if the Wi-Fi is not configured or if the Wi-Fi is already
    active.

    Args:
        interface (str): The name of the network interface to use.
        interval (int, optional): The interval in seconds to wait before
            retrying the connection. Default is 900 seconds.

    Raises:
        nmwifi.exceptions.InvalidConnectionParameters: If the interval is less
            than 90 seconds.

    Returns:
        NoReturn
    """

    if interval < 90:
        raise exceptions.InvalidConnectionParameters(
            "Interval must be at least 90 seconds."
        )

    while True:
        try:
            actions.activate_wifi(interface)
        except exceptions.NotConfigured:
            pass

        time.sleep(interval)
