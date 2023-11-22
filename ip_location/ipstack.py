from json import JSONDecodeError
from typing import Union

import httpx
from dotenv import load_dotenv
from pydantic import ValidationError

from ip_location.schema import Coordinates, IPStackError, IPStackErrorInfo

load_dotenv()


def get_coordinates(api_key: str, ip_address: str) -> Union[IPStackError, Coordinates]:
    url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}&fields=latitude,longitude"
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()

    try:
        return IPStackError.model_validate(response.json())
    except ValidationError:
        return Coordinates.model_validate(response.json())
    except JSONDecodeError:
        return IPStackError(error=IPStackErrorInfo(info="Unable to decode IPStack response."))
