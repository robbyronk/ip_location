import os
import sys

import typer

from ip_location.ip_address import is_valid_ip
from ip_location.ipstack import get_coordinates
from ip_location.schema import IPStackError

app = typer.Typer()


@app.command()
def main(ip_address: str = typer.Argument(None, help="The IP address to query. Omit or use '-' to read from stdin."),
         api_key: str = typer.Option(
             None,
             "--api-key",
             help="Your IPStack API key. Can also be provided via IPSTACK_API_KEY environment variable"
         )):
    api_key = api_key or os.getenv("IPSTACK_API_KEY")

    if not api_key:
        typer.echo(
            "Error: Please provide an IPStack API key via --api-key option or IPSTACK_API_KEY environment variable",
            err=True
        )
        sys.exit(2)

    if ip_address in ["-", None]:
        ip_address = sys.stdin.readline().strip()
    elif not ip_address:
        typer.echo("Error: Please provide an IP address or use '-' to read from stdin.", err=True)
        sys.exit(2)
    if not is_valid_ip(ip_address):
        typer.echo("Error: Please provide a valid IP address.", err=True)
        sys.exit(2)

    try:
        coordinates = get_coordinates(api_key, ip_address)
    except:
        # catch all here to prevent stack traces from flowing into downstream tools
        typer.echo(f"Error: Unknown error.", err=True)
        sys.exit(1)

    if isinstance(coordinates, IPStackError):
        typer.echo(f"Error: {coordinates.error.info}", err=True)
        sys.exit(1)

    typer.echo(f"{coordinates.latitude},{coordinates.longitude}")


if __name__ == "__main__":
    app()
