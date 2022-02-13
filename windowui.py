from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui/WindowUI.ui", self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec())
