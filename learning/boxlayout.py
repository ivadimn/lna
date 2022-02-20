from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QLabel, QLineEdit,QWidget, QPushButton, QMenu, QApplication, QHBoxLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI BoxLayout")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox = QHBoxLayout()

        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click two")
        btn3 = QPushButton("Click three")
        btn4 = QPushButton("Click four")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        #hbox.addSpacing(100)
        hbox.addStretch(5)

        self.setLayout(hbox)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())