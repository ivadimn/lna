from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QIcon, QImage, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI SpinBox")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox = QHBoxLayout()

        label = QLabel("Laptop pricing")
        label.setFont(QFont("Times", 15))

        self.lineedit = QLineEdit()

        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.total_price = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_price)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineedit.text() != 0:
            price = int(self.lineedit.text())
            total_price = self.spinbox.value()  * price
            self.total_price.setText(str(total_price))
        else:
            print("wrong price value")


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
