import sys

from Model.Network import Network
from Layouts.sidebar import Sidebar
from Widgets.title import Title
from Widgets.neuralNet import NeuralNetwork
from Widgets.settings import Settings

from PyQt6.QtWidgets import *
import matplotlib.pyplot as plt
import networkx as nx

# constants
APP_NAME = "Neural Network Visualizer"

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(APP_NAME)

        title = Title(APP_NAME)
        neural_net = NeuralNetwork(nx.Graph(), plt.figure(), Network())
        neural_net_config = Settings(neural_net)
        sidebar = Sidebar(title, neural_net_config)

        main_layout = QHBoxLayout()
        main_layout.addLayout(sidebar)
        main_layout.addWidget(neural_net)

        content = QWidget()
        content.setLayout(main_layout)
        self.setCentralWidget(content)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()