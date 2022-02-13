from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit,QWidget



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon("images/python.png"))
        """
        label = QLabel("Python GUI Development", self)
        label.move(100, 100)
        label.setFont(QFont("Times", 18))
        label.setStyleSheet("color:red")

        label.setNum(63637)
        

        label = QLabel(self)
        pixmap = QPixmap("images/python.png")
        label.setPixmap(pixmap)
        """

        label = QLabel(self)
        movie = QMovie("images/sky.gif")
        label.setMovie(movie)
        movie.start()


