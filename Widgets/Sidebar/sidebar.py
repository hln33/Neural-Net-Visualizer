from Model.network import Network

from .networkInfo import NetworkInfo
from .settings import Settings
from Widgets.neuralNet import NeuralNetwork
from Widgets.title import Title

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Sidebar(QWidget):
    def __init__(self, model: Network, graph: NeuralNetwork) -> None:
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(_SettingsSection(graph))
        layout.addWidget(_InfoSection(model))
        self.setLayout(layout)


class _SettingsSection(QWidget):
    def __init__(self, graph: NeuralNetwork):
        super().__init__()

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(Title("Settings"))
        settings_layout.addWidget(Settings(graph.add_layer))

        self.setLayout(settings_layout)


class _InfoSection(QWidget):
    def __init__(self, model: Network):
        super().__init__()

        layout = QGridLayout()

        title = Title("Info")
        title.setAutoFillBackground(True)
        palette = title.palette()
        palette.setColor(title.backgroundRole(), QColor('red'))
        title.setPalette(palette)

        info = NetworkInfo(model)
        info.setContentsMargins(1, 1, 1, 1)

        layout.addWidget(title, 0, 0)
        layout.addWidget(info, 1, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
