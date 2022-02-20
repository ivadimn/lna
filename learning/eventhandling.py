from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QLabel, QLineEdit,QWidget, QPushButton, QMenu, QApplication, QHBoxLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI Event handling")
        self.setWindowIcon(QIcon("images/python.png"))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Chnage Text")
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Default text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Another text")
        self.label.setFont(QFont("Times", 14))
        self.label.setStyleSheet("color:red")

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())