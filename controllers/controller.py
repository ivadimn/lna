from abc import ABC, abstractmethod
from typing import List


class Controller(ABC):

    @abstractmethod
    def get_data(self) -> List[tuple]: ...

    @abstractmethod
    def add_data(self, data: List[tuple]) -> bool: ...

    @abstractmethod
    def delete_data(self, data: List[tuple]) -> bool: ...

