from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Title(QWidget):
    def __init__(self, title_text, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft) -> None:
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        title = QLabel(title_text)
        title.setAlignment(alignment)
        layout.addWidget(title)
