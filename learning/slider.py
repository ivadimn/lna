from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QHBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Slider Qt Window")
        self.setWindowIcon(QIcon("../images/python.png"))

        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(5)
        self.slider.setMaximum(100)
        self.slider.setMinimum(0)
        self.slider.valueChanged.connect(self.value_changed)

        self.label = QLabel()
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def value_changed(self):
        value = self.slider.value()
        self.label.setText(str(value))


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())