import sys
import time

from Widgets.title import Title
from Widgets.network import Network

from PyQt6.QtWidgets import *
import matplotlib.pyplot as plt
import networkx as nx

# constants
_APP_NAME = "Neural Network"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(_APP_NAME)
        title_widget = Title(_APP_NAME)
        neural_net_widget = Network(nx.Graph(), plt.figure())
        
        neural_net_widget.add_layer(3)
        neural_net_widget.add_layer(3)
        neural_net_widget.add_layer(3)

        layout = QVBoxLayout()
        layout.addWidget(title_widget)
        layout.addWidget(neural_net_widget)

        content = QWidget()
        content.setLayout(layout)
        self.setCentralWidget(content)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()