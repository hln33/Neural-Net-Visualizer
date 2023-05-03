from Model.network import Network

from PyQt6.QtWidgets import *

class NetworkInfo(QWidget):
    def __init__(self, model: Network) -> None:
        super().__init__()

        self.model = model
    
        layout = QVBoxLayout()
        numLayers = str(len(model.layers))
        layout.addWidget(QLabel(numLayers))
        self.setLayout(layout)