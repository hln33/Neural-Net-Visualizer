from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Title(QLabel):
    def __init__(self, title_text: str, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft) -> None:
        super().__init__()

        self.setText(title_text)
        self.setAlignment(alignment)
