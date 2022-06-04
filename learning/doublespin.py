from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi("../ui/doublespin.ui", self)
        self.price_edit = self.findChild(QLineEdit, "price_edit")
        self.spinbox = self.findChild(QDoubleSpinBox, "spinbox")
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.total_price = self.findChild(QLineEdit, "total_price")


    def spin_selected(self):
        if self.price_edit.text() != 0:
            price = int(self.price_edit.text())
            total_price = price * self.spinbox.value()
            self.total_price.setText(str(total_price))
        else:
            print("wrong price")


app = QApplication([])
window = UI()
window.show()
sys.exit(app.exec())