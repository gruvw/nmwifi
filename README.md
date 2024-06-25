# nmwifi

The [Python](https://www.python.org) package `nmwifi` provides an API (and a CLI) to configure a Wi-Fi device through [NetworkManager](https://networkmanager.dev/) using a fallback Access Point.

Take a look at the project's [roadmap](docs/roadmap.md) to see upcoming features (and all the work accomplished).

**Note** - Check out the `nmwifi` python package on PyPI: <https://pypi.org/project/nmwifi> (managed using [Poetry](https://python-poetry.org/)).

This package was initially developed for RPI to set up a Wi-Fi connection to a home router. 
However it works for any device that has at least one wireless network interface and that has NetworkManager installed.

## Installation

- Install by running: `pip install nmwifi`
- Usage: `nmwifi --help`

### Basic usage

The most common usage of the `nmwifi` tool is to call `setup` and then keep the `balance` loop running forever.
This will set up a Wi-Fi connection to a given SSID and password along with an Access Point (with default SSID and no password).
The device will continuously try to connect to the specified Wi-Fi network.
When the Wi-Fi network is not available, it will automatically switch to the Access Point (AP).
The balance loop will periodically try to reconnect to the Wi-Fi network on AP mode.

#### CLI

```bash
nmwifi setup -i <network-interface> --ws <wifi-ssid> -wp <wifi-password>
nmwifi balance -i <network-interface>
```

#### Python

```python
import nmwifi

nmwifi.setup("<network-interface>", "<wifi-ssid>", "<wifi-password>")
nmwifi.balance("<network-interface>")
```

## Contributions

Feel free to contribute by submitting pull requests, whether to add new features, improve existing functionality, or fix bugs :)

Before opening a new PR, make sure to open an issue to discuss it beforehand (first check if a similar issue does not already exist).

## Powered by

This project would not be possible without the wonderful technologies below:

* [Python](https://www.python.org/)
* [NetworkManager](https://networkmanager.dev/)
