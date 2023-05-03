from typing import Callable

from PyQt6.QtWidgets import *

# constants
MIN_LAYER_SIZE = 1
MAX_LAYER_SIZE = 10
ADD_LAYER_BUTTON_TEXT = "Add Layer"

class Settings(QWidget):
    def __init__(self, add_layer_func: Callable[[int], None]) -> None:
        super().__init__()
        
        self.add_layer_func = add_layer_func
        self.new_Layer_size = MIN_LAYER_SIZE

        add_layer_button = QPushButton(ADD_LAYER_BUTTON_TEXT)
        add_layer_button.clicked.connect(self._add_network_layer)

        layer_size_picker = QSpinBox()
        layer_size_picker.setRange(MIN_LAYER_SIZE, MAX_LAYER_SIZE)
        layer_size_picker.lineEdit().setReadOnly(True)
        layer_size_picker.valueChanged.connect(self._set_new_layer_size)

        layout = QVBoxLayout()
        layout.addWidget(layer_size_picker)
        layout.addWidget(add_layer_button)
        self.setLayout(layout)

    def _add_network_layer(self) -> None:
        self.add_layer_func(self.new_Layer_size)
    
    def _set_new_layer_size(self, size: int) -> None:
        assert size <= MAX_LAYER_SIZE, "layer size must be less than or equal max size"
        assert size >= MIN_LAYER_SIZE, "layer size must be greater than or equal min size"

        self.new_Layer_size = size
