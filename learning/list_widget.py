from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Base Qt Window")
        self.setWindowIcon(QIcon("../images/python.png"))

        vbox = QVBoxLayout()
        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "C")
        self.list_widget.insertItem(3, "C++")
        self.list_widget.insertItem(4, "C#")
        self.list_widget.insertItem(5, "GOLang")
        self.list_widget.insertItem(6, "Fortran")
        self.list_widget.insertItem(7, "Pascal")
        self.list_widget.insertItem(8, "JavaScript")
        self.list_widget.insertItem(9, "Rust")
        self.list_widget.insertItem(10, "Go")

        vbox.addWidget(self.list_widget)
        self.setLayout(vbox)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())