from typing import List
from controllers.controller import  Controller
from repositories.rp_repository import RpRepository
from model_data.model import Rp


class RpController(Controller):

    def get_data(self) -> List[tuple]:
        rep = RpRepository()
        lst = []
        for rp in rep.select(()):
            lst.append(rp.row())
        return lst

    def add_data(self, data: List[tuple]) -> bool:
        lst = []
        for rp in data:
            lst.append(Rp(*rp))
        rep = RpRepository()
        return True if rep.insert(lst) > 0 else False

    def delete_data(self, data: List[tuple]) -> bool:
        rep = RpRepository()
        params = tuple(row[0] for row in data)
        return True if rep.delete(params) > 0 else False
