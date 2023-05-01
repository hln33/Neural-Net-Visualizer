import sys

from Widgets.title import Title
from Widgets.network import Network
from Widgets.networkConfig import NetworkConfig

from PyQt6.QtWidgets import *
import matplotlib.pyplot as plt
import networkx as nx

# constants
APP_NAME = "Neural Network Visualizer"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.title = Title(APP_NAME)
        self.neural_net = Network(nx.Graph(), plt.figure())
        self.neural_net_config = NetworkConfig(self.neural_net)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.neural_net)
        layout.addWidget(self.neural_net_config)

        content = QWidget()
        content.setLayout(layout)
        self.setCentralWidget(content)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()