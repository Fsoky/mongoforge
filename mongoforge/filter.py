from typing import Any
from .types import MagicData


class Field:
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, value: Any) -> MagicData:
        return {self.name: value}

    def __gt__(self, value: Any) -> MagicData:
        return {self.name: {"$gt": value}}

    def __lt__(self, value: Any) -> MagicData:
        return {self.name: {"$lt": value}}

    def __ge__(self, value: Any) -> MagicData:
        return {self.name: {"$gte": value}}

    def __le__(self, value: Any) -> MagicData:
        return {self.name: {"$lte": value}}

    def in_(self, values: list | tuple | set) -> MagicData:
        return {self.name: {"$in": list(values)}}


class Filter:
    
    def __getattr__(self, name: str):
        return Field(name)

    def or_f(self, *filters: Any) -> MagicData:
        return {"$or": list(filters)}