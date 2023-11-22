# IP Location

Fetches the latitude and longitude of a given IP address from IPStack.

```
 Usage: main.py [OPTIONS] [IP_ADDRESS]                                                                                                                                                                         
                                                                                                                                                                                                               
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   ip_address      [IP_ADDRESS]    The IP address to query. Omit or use '-' to read from stdin.                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --api-key                   TEXT  Your IPStack API key. Can also be provided via IPSTACK_API_KEY environment variable│
│ --help                            Show this message and exit.                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Example usage:

```
docker run -it --rm ip_location 8.8.8.8
```

Example output:
```
40.5369987487793,-82.12859344482422
```

## Security Notice

The IPstack free plan does not allow https requests. Responses from IPStack could be manipulated by a man-in-the-middle
attack.

## Setup

Sign up for an IPStack API key if you haven't already at [https://ipstack.com](https://ipstack.com).

Create `.env` and add your API key.

```shell
touch .env
echo "IPSTACK_API_KEY=your_api_key" >> .env
```

## Run with Docker

Build the image using:

```shell
docker build -t ip_location .
```

Run the container to get the coordinates for an IP address (replace `8.8.8.8` with your choice of IP):

```shell
docker run -it --rm ip_location 8.8.8.8
```

To pass an API key as an environment variable (replace `8.8.8.8` with your choice of IP):

```shell
docker run -e "IPSTACK_API_KEY=your_api_key" -it --rm ip_location 8.8.8.8
```

## Library Choices

- Typer: Easier to use than the builtin `argparse`.
- HTTPX: Easier to use than the builtin `urllib`.
- python-dotenv: Allows the use of a `.env` to set environment variables.
- Pydantic: Robust parser and data validator.
