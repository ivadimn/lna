from sqlite3 import Error
from typing import List
from repositories.repository import Repository
from model_data.model import Rp
from generators import sql
from database.db import Db


class RpRepository(Repository):

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

    def insert(self, entities: List[Rp]) -> int:
        try:
            list_values = []
            for rp in entities:
                list_values.append((rp.id, rp.name, rp.full_name))
            sql_insert = sql.gen_insert(Rp, "orgs", autoincrement=False)
            row_id = Db.insert(sql_insert, list_values)
            return row_id
        except Error as err:
            print(str(err))
            return -1

    def delete(self, params: dict) -> None:
        pass