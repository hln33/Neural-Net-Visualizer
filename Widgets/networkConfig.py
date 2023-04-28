from PyQt6.QtWidgets import *

# constants
MIN_LAYER_SIZE = 1
MAX_LAYER_SIZE = 10

class NetworkConfig(QWidget):
    def __init__(self, network):
        super().__init__()
        
        self.network = network
        self.new_Layer_size = MIN_LAYER_SIZE

        add_layer_button = QPushButton("Add Layer")
        add_layer_button.clicked.connect(self._add_network_layer)

        layer_size_picker = QSpinBox()
        layer_size_picker.setRange(MIN_LAYER_SIZE, MAX_LAYER_SIZE)
        layer_size_picker.lineEdit().setReadOnly(True)
        layer_size_picker.valueChanged.connect(self._set_new_layer_size)

        layout = QVBoxLayout()
        layout.addWidget(add_layer_button)
        layout.addWidget(layer_size_picker)
        self.setLayout(layout)

    def _add_network_layer(self):
        self.network.add_layer(self.new_Layer_size)
    
    def _set_new_layer_size(self, size):
        self.new_Layer_size = size
