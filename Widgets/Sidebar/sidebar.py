from Model.network import Network

from .networkInfo import NetworkInfo
from .settings import Settings
from Widgets.neuralNet import NeuralNetwork
from Widgets.title import Title

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Sidebar(QVBoxLayout):
    def __init__(self, model: Network, graph: NeuralNetwork) -> None:
        super().__init__()

        self.addWidget(SettingsSection(graph))
        self.addWidget(InfoSection(model))


class SettingsSection(QWidget):
    def __init__(self, graph: NeuralNetwork):
        super().__init__()

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(Title("Settings"))
        settings_layout.addWidget(Settings(graph.add_layer))
        self.setLayout(settings_layout)


class InfoSection(QWidget):
    def __init__(self, model: Network):
        super().__init__()

        info_layout = QVBoxLayout()

        info_title = Title("Info")
        info_title.setContentsMargins(0, 0, 0, 0)
        info_title.setAutoFillBackground(True)
        palette = info_title.palette()
        palette.setColor(info_title.backgroundRole(), QColor('red'))
        info_title.setPalette(palette)

        info_layout.addWidget(info_title)
        info_layout.addWidget(NetworkInfo(model))
        info_layout.setSpacing(0)
        info_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(info_layout)
