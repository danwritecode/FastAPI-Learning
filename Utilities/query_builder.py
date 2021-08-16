from abc import ABCMeta, abstractmethod
from typing import List
from pydantic.dataclasses import dataclass

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def set_entity():
        "Build part a"

    @staticmethod
    @abstractmethod
    def create_filters():
        "Build part a"

    @staticmethod
    @abstractmethod
    def add_sorting():
        "Build part b"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.query = Query()

    def set_entity(self, entity):
        self.query.entity = entity
        return self

    def create_filters(self, filters):
        self.query.filters = filters
        return self

    def get_result(self):
        return self.query

class Query():
    """The Filters and sorters"""

    def __init__(self):
        self.entity: str = None
        self.filters: list = None
    
    def assembled_query(self):
        if self.filters is None and self.sorters is None:
            return f"SELECT * FROM {self.entity}"
        if self.filters is not None:
            if len(self.filters > 1):
                return f"""
                    Select *
                    From {self.entity}
                    Where {self.filters[0].field_name} = {self.filters[0].field_value}
                """

@dataclass
class Filter:
    field_name: str
    field_value: str

@dataclass
class Sorter:
    field_name: str
    sort_desc: bool


class SelectQueryDirector:
    """Query Director used to build complex Select Statements"""

    @staticmethod
    def construct(entity: str, filters: List[Filter], sorters: List[Filter]):
        "Constructs and returns the final product"
        return Builder()\
            .set_entity(entity)\
            .create_filters(filters)\
            .get_result()


if __name__ == "__main__":
    filters = [
        Filter("Name", "Dan")
    ]

    QUERY = SelectQueryDirector.construct("User", filters)
    print(QUERY.assembled_query())