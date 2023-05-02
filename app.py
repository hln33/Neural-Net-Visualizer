import sys

from Model.Network import Network
from Widgets.Sidebar.sidebar import Sidebar
from Widgets.neuralNet import NeuralNetwork

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import matplotlib.pyplot as plt
import networkx as nx

# constants
APP_NAME = "Neural Network Visualizer"

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(APP_NAME)

        model = Network()
        graph = NeuralNetwork(nx.Graph(), plt.figure(), model)
        sidebar = Sidebar(model, graph)

        main_layout = QHBoxLayout()
        main_layout.addLayout(sidebar)
        main_layout.addWidget(graph)

        content = QWidget()
        content.setLayout(main_layout)
        self.setCentralWidget(content)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()