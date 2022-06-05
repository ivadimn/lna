from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Base Qt Window")
        self.setWindowIcon(QIcon("../images/python.png"))
        vbox = QVBoxLayout()

        self.lcd_number = QLCDNumber()
        self.lcd_number.setStyleSheet("background:red")

        vbox.addWidget(self.lcd_number)
        self.setLayout(vbox)
        self.show_lcd()

        timer = QTimer(self)
        timer.timeout.connect(self.show_lcd)
        timer.start(1000)

    def show_lcd(self):
        #time = QTime.currentTime()
        #time_str = time.toString("hh:mm:ss")
        self.counter += 1
        self.lcd_number.display(str(self.counter))

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())