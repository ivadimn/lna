from typing import List
from controllers.controller import  Controller
from repositories.rp_repository import RpRepository
from model_data.model import Rp


class RpController(Controller):

    def get_data(self) -> List[Rp]:
        rep = RpRepository()
        lst = [rp for rp in rep.select(())]
        return lst

    def add_data(self, data: List[Rp]) -> bool:
        lst = []
        for rp in data:
            lst.append(rp)
        rep = RpRepository()
        return True if rep.insert(lst) > 0 else False

    def delete_data(self, data: List[Rp]) -> bool:
        rep = RpRepository()
        return True if rep.delete(data) > 0 else False
