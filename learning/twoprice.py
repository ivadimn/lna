from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox, QSpinBox, QLabel
from PyQt6 import uic
import sys


class UI(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi("../ui/twoprice.ui", self)
        self.le_pen_price: QLineEdit = self.findChild(QLineEdit, "le_pen_price")
        self.le_shugar_price: QLineEdit = self.findChild(QLineEdit, "le_shugar_price")
        self.spinbox = self.findChild(QSpinBox, "spinbox")
        self.dspinbox = self.findChild(QDoubleSpinBox, "dspinbox")
        self.spinbox.editingFinished.connect(self.first_price)
        self.dspinbox.editingFinished.connect(self.second_price)
        self.le_total_pen_price: QLineEdit = self.findChild(QLineEdit, "le_total_pen_price")
        self.le_total_shugar_price: QLineEdit = self.findChild(QLineEdit, "le_total_shugar_price")
        self.lbl_result = self.findChild(QLabel, "lbl_result")


    def first_price(self):
        if self.le_pen_price.text() != 0:
            price = int(self.le_pen_price.text())
            total_price = price * self.spinbox.value()
            self.le_total_pen_price.setText(str(total_price))
        else:
            print("wrong price")

    def second_price(self):
        if self.le_shugar_price.text() != 0:
            price = int(self.le_shugar_price.text())
            total_price = price * self.dspinbox.value()
            self.le_total_shugar_price.setText(str(total_price))

            two_total_price = total_price + int(self.le_total_pen_price.text())
            self.lbl_result.setText(str(two_total_price))
        else:
            print("wrong price")


app = QApplication([])
window = UI()
window.show()
app.exec()
