from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QLabel, QLineEdit,QWidget, QPushButton, QMenu, QApplication, QVBoxLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI BoxLayout")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()

        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click two")
        btn3 = QPushButton("Click three")
        btn4 = QPushButton("Click four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())