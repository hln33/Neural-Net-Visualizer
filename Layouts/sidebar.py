from PyQt6.QtWidgets import *

class Sidebar(QVBoxLayout):
    def __init__(self, title, settings):
        super().__init__()

        self.addWidget(title)
        self.addWidget(settings)