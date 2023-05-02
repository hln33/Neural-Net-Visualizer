from Model.Network import Network

from Widgets.Sidebar.networkInfo import NetworkInfo
from Widgets.Sidebar.settings import Settings
from Widgets.neuralNet import NeuralNetwork
from Widgets.title import Title

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Sidebar(QVBoxLayout):
    def __init__(self, model: Network, graph: NeuralNetwork) -> None:
        super().__init__()
        
        settings_section = QWidget()
        settings_layout = QVBoxLayout()
        settings_layout.addWidget(Title("Settings"))
        settings_layout.addWidget(Settings(graph))
        settings_section.setLayout(settings_layout)

        info_section = QWidget()
        info_layout = QVBoxLayout()
        info_layout.addWidget(Title("Info"))
        info_layout.addWidget(NetworkInfo(model))
        info_section.setLayout(info_layout)

        self.addWidget(settings_section)
        self.addWidget(info_section)
        