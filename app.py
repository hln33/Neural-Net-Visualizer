import sys
from Components.title import Title
from PyQt6.QtWidgets import *

_APP_NAME = "Neural Network"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(_APP_NAME)
        self.setCentralWidget(Title(_APP_NAME))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()