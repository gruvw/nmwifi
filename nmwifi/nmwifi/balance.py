import time

from . import _nm_wrapper, actions, exceptions


@_nm_wrapper.verify_interface
def balance(interface, interval=900):
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
