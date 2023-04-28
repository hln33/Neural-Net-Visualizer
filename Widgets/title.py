from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Title(QWidget):
    def __init__(self, title_text):
        super(Title, self).__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        title = QLabel(title_text)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
