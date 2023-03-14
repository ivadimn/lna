from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Entity(ABC):
    id: int

    @abstractmethod
    def row(self) -> tuple: ...


@dataclass
class Rp(Entity):
    name: str
    full_name: str

    def row(self) -> tuple:
        return str(self.id), self.name, self.full_name

