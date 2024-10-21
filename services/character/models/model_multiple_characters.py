from pydantic import BaseModel, HttpUrl
from typing import Optional

class Origin(BaseModel):
    name: str
    url: Optional[HttpUrl | str]

class Location(BaseModel):
    name: str
    url: Optional[HttpUrl | str]

class MultipleCharactersModel(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: Optional[str]
    gender: str
    origin: Origin
    location: Location
    image: HttpUrl
    episode: list[HttpUrl]
    url: HttpUrl
    created: str