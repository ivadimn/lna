from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QAction
from PyQt6.QtWidgets import QStatusBar, QPushButton, QMainWindow
from PyQt6.QtWidgets import QWidget, QTabWidget, QLabel, QMenuBar, QMenu, QToolBar, QTabBar
from PyQt6.QtCore import QSize, Qt
from ui.rp_table import RpTable

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

        rp_action = QAction(QIcon("images/table.png"), "Разделы персонала", self)
        rp_action.setStatusTip("Посмотреть разделы персонала")
        rp_action.triggered.connect(self.on_rp_action_event)
        toolbar.addAction(rp_action)

        os_action = QAction(QIcon("images/tree.png"), "Орг. структура", self)
        os_action.setStatusTip("Посмотреть организационную структуру")
        os_action.triggered.connect(self.on_rp_action_event)
        toolbar.addAction(os_action)
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&Струкутура")
        file_menu.addAction(rp_action)

    def create_buttons(self):
        btn_add = QPushButton("Add Tab")
        btn_del = QPushButton("Delete Tab")
        #self.hbox.addWidget(btn_add)
        #self.hbox.addWidget(btn_del)

    def create_menu(self) -> QMenuBar:
        menuBar = QMenuBar(self)
        menuFile = QMenu("&Структура", menuBar)
        rp_action = QAction("Разделы персонала")
        menuFile.addAction("Разделы персонала")
        menuBar.addMenu(menuFile)
        return menuBar

    def on_rp_action_event(self, s):
        rp_table = RpTable()
        #self.tab.addTab("Разделы персонала")
        self.tab.addTab(rp_table, "Разделы персонала")

        print("click", s)
        #dlg = RpDialog(save_rp)
        #print(dlg.exec())

    def close_tab(self, index: int):
        self.tab.removeTab(index)

