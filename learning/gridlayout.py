from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QLabel, QLineEdit,QWidget, QPushButton, QMenu, QApplication, QGridLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI BoxLayout")
        self.setWindowIcon(QIcon("images/python.png"))

        grid = QGridLayout()

        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click two")
        btn3 = QPushButton("Click three")
        btn4 = QPushButton("Click four")
        btn5 = QPushButton("Click five")
        btn6 = QPushButton("Click six")
        btn7 = QPushButton("Click seven")
        btn8 = QPushButton("Click eight")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())