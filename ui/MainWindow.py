from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit,QWidget, QPushButton, QMenu
from PyQt6.QtCore import QSize



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI QLineEdit")
        self.setWindowIcon(QIcon("images/python.png"))
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Courier", 12, QFont.Weight.DemiBold))
        #line_edit.setText("Default text")
        #line_edit.setPlaceholderText("Enter your name...")
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        #self.create_button()

    """def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100, 100, 130, 40)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/python.png"))
        btn.setIconSize(QSize(32, 32))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Arial", 12, QFont.Weight.ExtraBold))
        menu.setStyleSheet("background-color:blue")
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)"""
