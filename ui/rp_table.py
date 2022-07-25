from PyQt6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QIcon, QAction
from ui.rp_dialog import RpDialog
from repositories.rp_repository import RpRepository
from model_data.model import Rp

class RpTable(QWidget):

    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Идентификатор", "Наименование", "Организация"])


        new_button = QPushButton(QIcon("images/new.png"), "Добавить")
        new_button.clicked.connect(self.on_add_rp)
        edit_button = QPushButton(QIcon("images/exit.png"), "Изменить")
        del_button = QPushButton(QIcon("images/cut.png"), "Удалить")

        hbox = QHBoxLayout()
        hbox.addWidget(new_button)
        hbox.addWidget(edit_button)
        hbox.addWidget(del_button)
        hbox.addSpacing(100)

        vbox.addWidget(self.table)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def on_add_rp(self):
        dlg = RpDialog(self.update_data)
        print(dlg.exec())

    def update_data(self,  data: tuple) -> None:
        index = self.table.rowCount()
        self.table.insertRow(index)
        list_rp = [Rp(*data)]
        RpRepository().insert(entities=list_rp)
        for j, d in enumerate(data):
            item = QTableWidgetItem(f"{d}")
            self.table.setItem(index, j, item)

    def fill_table(self, data: list) -> None:
        pass

