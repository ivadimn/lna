from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QLabel, QWidget, QApplication, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI Radio buttons")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon("../images/py.png"))
        self.check1.setIconSize(QSize(40, 40))
        self.check1.setFont(QFont("Arial", 14))

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon("../images/java.png"))
        self.check2.setIconSize(QSize(40, 40))
        self.check2.setFont(QFont("Arial", 14))

        self.check3 = QCheckBox("JavaScript")
        self.check3.setIcon(QIcon("../images/javascript.png"))
        self.check3.setIconSize(QSize(40, 40))
        self.check3.setFont(QFont("Arial", 14))

        self.check1.stateChanged.connect(self.item_selected)
        self.check2.stateChanged.connect(self.item_selected)
        self.check3.stateChanged.connect(self.item_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Arial", 16))

        vbox = QVBoxLayout()

        hbox.addWidget(self.check1)
        hbox.addWidget(self.check2)
        hbox.addWidget(self.check3)

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


    def item_selected(self):
        value = ""
        if self.check1.isChecked():
            value = self.check1.text()
        if self.check2.isChecked():
            value = self.check2.text()
        if self.check3.isChecked():
            value = self.check3.text()

        self.label.setText(value)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())