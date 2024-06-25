import click

import nmwifi


interface_option = click.option(
    "-i",
    "--interface",
    type=str,
    required=True,
    help="Network interface to use for the connections. (see `nmcli d`)",
)
ap_ssid_option = click.option(
    "-as",
    "--ap-ssid",
    type=str,
    help="SSID of the Access Point network.",
)
ap_password_option = click.option(
    "-ap",
    "--ap-password",
    type=str,
    help="Password of the Access Point network.",
)
wifi_ssid_option = click.option(
    "-ws",
    "--wifi-ssid",
    type=str,
    help="SSID of the Wi-Fi network.",
)
wifi_password_option = click.option(
    "-wp",
    "--wifi-password",
    type=str,
    help="Password of the Wi-Fi network.",
)
activate_option = click.option(
    "-a/-na",
    "--activate/--no-activate",
    default=True,
    show_default=True,
    help="Whether to activate newly created connections by default.",
)


@click.group()
def cli():
    pass


@cli.command(
    help="Set up both the Access Point and Wi-Fi NetworkManager connections.",
)
@interface_option
@wifi_ssid_option
@wifi_password_option
@ap_ssid_option
@ap_password_option
@activate_option
def setup(
    interface,
    wifi_ssid,
    wifi_password,
    ap_ssid,
    ap_password,
    activate,
):
    nmwifi.setup(
        interface,
        wifi_ssid,
        wifi_password,
        ap_ssid,
        ap_password,
        activate,
    )


@cli.command(
    help="Set up the Wi-Fi NetworkManager connection.",
)
@interface_option
@wifi_ssid_option
@wifi_password_option
@activate_option
def setup_wifi(
    interface,
    wifi_ssid,
    wifi_password,
    activate,
):
    nmwifi.setup_wifi(
        interface,
        wifi_ssid,
        wifi_password,
        activate,
    )


@cli.command(
    help="Set up the Access Point NetworkManager connection.",
)
@interface_option
@ap_ssid_option
@ap_password_option
@activate_option
def setup_ap(
    interface,
    wifi_ssid,
    wifi_password,
    activate,
):
    nmwifi.setup_ap(
        interface,
        wifi_ssid,
        wifi_password,
        activate,
    )


@cli.command(
    help="Periodically retries to connect to the Wi-Fi connection on AP mode.",
)
@interface_option
@click.option(
    "-t",
    "--time",
    type=int,
    default=900,
    show_default=True,
    help="Interval in seconds between retries. (minimum 90)",
)
def balance(interface, time):
    nmwifi.balance(interface, time)


@cli.command(
    help="Removes all nmwifi related connections created on NetworkManager.",
)
def clean():
    nmwifi.clean()
