from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableView)
from PyQt6.QtGui import QIcon, QAction, QStandardItemModel, QStandardItem
from ui.rp_dialog import RpDialog
from ui.models.rp_model import RpModel
from repositories.rp_repository import RpRepository
from model_data.model import Rp
from controllers.rp_controller import RpController
from resources.main_res import rp_res


class RpTable(QWidget):

    def __init__(self):
        super().__init__()
        self.model = None
        self.table_view = None
        self.initialize_ui()

    def initialize_ui(self):
        vbox = QVBoxLayout()

        new_button = QPushButton(QIcon(rp_res["ADD_EVENT"].icon), rp_res["ADD_EVENT"].title)
        new_button.setStatusTip(rp_res["ADD_EVENT"].status_tip)
        new_button.clicked.connect(self.on_add_rp)

        edit_button = QPushButton(QIcon(rp_res["EDIT_EVENT"].icon), rp_res["EDIT_EVENT"].title)
        edit_button.setStatusTip(rp_res["EDIT_EVENT"].status_tip)
        edit_button.clicked.connect(self.on_edit_rp)

        del_button = QPushButton(QIcon(rp_res["DELETE_EVENT"].icon), rp_res["DELETE_EVENT"].title)
        del_button.setStatusTip(rp_res["DELETE_EVENT"].status_tip)
        del_button.clicked.connect(self.on_del_rp)

        self.setup_model_view()

        hbox = QHBoxLayout()
        hbox.addWidget(new_button)
        hbox.addWidget(edit_button)
        hbox.addWidget(del_button)
        hbox.addSpacing(200)

        vbox.addWidget(self.table_view)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def setup_model_view(self):
        self.model = RpModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        #self.model.setColumnCount(3)
        self.table_view.setColumnWidth(0, 50)
        self.table_view.setColumnWidth(1, 200)
        self.table_view.setColumnWidth(2, 250)
        #self.model.setHorizontalHeaderLabels(rp_res["HEADERS"])

        self._load_data()

    def _load_data(self) -> None:
        contr = RpController()
        for i, rp in enumerate(contr.get_data()):
            self.model.add_rp(rp)

    def on_add_rp(self):
        dlg = RpDialog(self.insert_data)
        print(dlg.exec())

    def insert_data(self, data: Rp) -> None:
        contr = RpController()
        if contr.add_data([data]):
            self.model.add_rp(data)

    def on_del_rp(self):
        index = self.table_view.selectedIndexes()[0]
        rp = self.model.get_rp(index)
        contr = RpController()
        if contr.delete_data([rp]):
            self.model.del_rp(index)

    def on_edit_rp(self):
        index = self.table_view.selectedIndexes()[0]
        rp = self.model.get_rp(index)
        dlg = RpDialog(data=rp)
        print(dlg.exec())
