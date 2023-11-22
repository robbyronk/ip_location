from pydantic import BaseModel


class IPStackErrorInfo(BaseModel):
    code: int = 0
    type: str = None
    info: str


class IPStackError(BaseModel):
    success: bool = False
    error: IPStackErrorInfo


class Coordinates(BaseModel):
    longitude: float
    latitude: float
