from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Base Qt Window")
        self.setWindowIcon(QIcon("../images/python.png"))

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()
        label = QLabel("Select account: ")
        self.combo = QComboBox()
        self.combo.addItem("Current account")
        self.combo.addItem("Deposit account")
        self.combo.addItem("Saving account")
        self.combo.currentTextChanged.connect(self.combo_changed)
        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.current_selected = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.current_selected)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def combo_changed(self):
        sel_text = self.combo.currentText()
        self.current_selected.setText("You selected a: {0}".format(sel_text))


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())