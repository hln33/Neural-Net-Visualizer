from Model.network import Network

from PyQt6.QtWidgets import *

from Widgets.title import Title

class NetworkInfo(QWidget):
    def __init__(self, model: Network) -> None:
        super().__init__()
        model.register(self.update_stats)

        self.num_layers = QLabel("0")
    
        layout = QVBoxLayout()
        layout.addWidget(Title("Num Layers"))
        layout.addWidget(self.num_layers)
        self.setLayout(layout)

    def update_stats(self, stats: dict):
        num = stats[Network.NUM_LAYERS]
        self.num_layers.setText(str(num))
        print(stats)