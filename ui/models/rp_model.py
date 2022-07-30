from PyQt6.QtCore import QModelIndex, QVariant, QAbstractTableModel, QObject, Qt
from model_data.model import Rp
from typing import List, Any
from resources.main_res import rp_res


class RpModel(QAbstractTableModel):

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.__list_rp: List[Rp] = []

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 3

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__list_rp)

    def data(self, index: QModelIndex, role: int = ...) -> QVariant:
        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            return self.getData(index.row(), index.column())
        return QVariant()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Vertical:
            return QVariant(section + 1)
        elif  0 <= section <= 2:
            return QVariant(rp_res["HEADERS"][section])
        else:
            QVariant()

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

    def add_rp(self, rp: Rp) -> bool:
        self.beginInsertRows(QModelIndex(), len(self.__list_rp), len(self.__list_rp))
        self.__list_rp.append(rp)
        self.endInsertRows()
        return True

    def del_rp(self, index: QModelIndex) -> bool:
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        self.__list_rp.pop(index.row())
        self.endRemoveRows()
        return True

    def get_rp(self, index: QModelIndex) -> Rp:
        return self.__list_rp[index.row()]

    def getData(self, row: int, column: int) -> QVariant:
        if column == 0:
            return QVariant(self.__list_rp[row].id)
        elif column == 1:
            return QVariant(self.__list_rp[row].name)
        elif column == 2:
            return QVariant(self.__list_rp[row].full_name)
        else:
            return QVariant()





