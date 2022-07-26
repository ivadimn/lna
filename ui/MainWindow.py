from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QStatusBar, QPushButton, QMainWindow
from PyQt6.QtWidgets import QTabWidget, QMenuBar, QMenu, QToolBar
from PyQt6.QtCore import QSize
from ui.rp_table import RpTable
from ui.actions import Action
from resources.main_res import main_res


def save_rp(data: tuple) -> None:
    print(data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checking data")
        self.setGeometry(200, 200, 900, 400)
        self.tab = QTabWidget()
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tab)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        rp_action = Action(main_res["RP_EVENT"], self)
        rp_action.setStatusTip(main_res["RP_EVENT"].status_tip)
        rp_action.triggered.connect(self.on_rp_action_event)

        toolbar.addAction(rp_action)

        os_action = Action(main_res["OS_EVENT"], self)
        os_action.triggered.connect(self.on_rp_action_event)
        toolbar.addAction(os_action)
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu("&Струкутура")
        file_menu.addAction(rp_action)

    def on_rp_action_event(self, s):
        rp_table = RpTable()
        self.tab.addTab(rp_table, main_res["RP_EVENT"].title)

    def close_tab(self, index: int):
        self.tab.removeTab(index)

