from Model.network import Network

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from Widgets.title import Title

class NetworkInfo(QWidget):
    def __init__(self, model: Network) -> None:
        super().__init__()
        model.register(self.update_stats)

        self.num_layers = QLabel("0")
        self.num_layers.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.num_layers.setContentsMargins(10, 0, 0, 0)

        title = Title("Num Layers")
        title.setContentsMargins(0, 0, 0, 0)
    
        layout = QHBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.num_layers)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def update_stats(self, stats: dict):
        num = stats[Network.NUM_LAYERS]
        self.num_layers.setText(str(num))
        print(stats)