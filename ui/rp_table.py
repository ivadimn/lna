from PyQt6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QIcon, QAction
from ui.rp_dialog import RpDialog
from repositories.rp_repository import RpRepository
from model_data.model import Rp
from controllers.rp_controller import RpController
from resources.main_res import rp_res


class RpTable(QWidget):

    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(rp_res["HEADERS"])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 250)

        new_button = QPushButton(QIcon(rp_res["ADD_EVENT"].icon), rp_res["ADD_EVENT"].title)
        new_button.setStatusTip(rp_res["ADD_EVENT"].status_tip)
        new_button.clicked.connect(self.on_add_rp)

        edit_button = QPushButton(QIcon(rp_res["EDIT_EVENT"].icon), rp_res["EDIT_EVENT"].title)
        edit_button.setStatusTip(rp_res["EDIT_EVENT"].status_tip)
        #edit_button.clicked.connect(self.on_add_rp)

        del_button = QPushButton(QIcon(rp_res["DELETE_EVENT"].icon), rp_res["DELETE_EVENT"].title)
        del_button.setStatusTip(rp_res["DELETE_EVENT"].status_tip)
        del_button.clicked.connect(self.on_del_rp)

        self.fill_data()

        hbox = QHBoxLayout()
        hbox.addWidget(new_button)
        hbox.addWidget(edit_button)
        hbox.addWidget(del_button)
        hbox.addSpacing(200)

        vbox.addWidget(self.table)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def fill_data(self) -> None:
        contr = RpController()
        index = 0
        for row in contr.get_data():
            self.table.insertRow(index)
            for j, d in enumerate(row):
                item = QTableWidgetItem(f"{d}")
                self.table.setItem(index, j, item)
            index += 1


    def on_add_rp(self):
        dlg = RpDialog(self.insert_data)
        print(dlg.exec())

    def insert_data(self, data: tuple) -> None:
        contr = RpController()
        index = self.table.rowCount()
        self.table.insertRow(index)
        if contr.add_data([data]):
            for j, d in enumerate(data):
                item = QTableWidgetItem(f"{d}")
                self.table.setItem(index, j, item)

    def on_del_rp(self):
        lst = []
        for item in  self.table.selectedItems():
            print(item.data(0))
        print(lst)
