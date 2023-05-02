#from Widgets.neuralNet import NeuralNetwork
#from Widgets.neuralNet import NeuralNetwork

# look at this:
# https://www.google.com/search?q=python+getting+import+error+in+one+file+but+not+the+other&rlz=1C5CHFA_enCA960CA960&oq=python+getting+import+error+in+one+file+but+not+the+other&aqs=chrome..69i57j33i160l2.7352j0j7&sourceid=chrome&ie=UTF-8

from PyQt6.QtWidgets import *

class NetworkInfo(QWidget):
    def __init__(self, network) -> None:
        super().__init__()

        self.network = network
