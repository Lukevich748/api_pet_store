from pydantic import BaseModel, HttpUrl
from typing import Optional



class Origin(BaseModel):
    name: str
    url: Optional[HttpUrl | str]

class Location(BaseModel):
    name: str
    url: Optional[HttpUrl | str]

class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: Origin
    location: Location
    image: HttpUrl
    episode: list[HttpUrl]
    url: HttpUrl
    created: str

class Info(BaseModel):
    count: int
    pages: int
    next: Optional[HttpUrl]
    prev: Optional[HttpUrl]

class AllCharactersModel(BaseModel):
    info: Info
    results: list[Character]