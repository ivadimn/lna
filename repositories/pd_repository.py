from sqlite3 import Error
from typing import List
from repositories.repository import Repository
from generators import sql
from model_data.model import Rp
from database.db import Db
from model_data.model import Pd


class PdRepository(Repository):

    def select(self, params: tuple) -> List[Rp]:
        if len(params) > 0:
            sql_select = sql.gen_select_by_id(Rp, "orgs", "id")
        else:
            sql_select = sql.gen_select_all(Rp, "orgs")
        rows = Db.select(sql_select, params)
        rp_list = list()
        for row in rows:
            rp_list.append(Rp(*row))
        return rp_list
