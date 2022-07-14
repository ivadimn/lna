from abc import ABC, abstractmethod
from typing import List
from model_data.model import Entity


class Repository(ABC):

    @abstractmethod
    def select(self, params: dict) -> List[Entity]: ...

    @abstractmethod
    def insert(self, entities: List[Entity]) -> None: ...

    @abstractmethod
    def delete(self, params: dict) -> None: ...






