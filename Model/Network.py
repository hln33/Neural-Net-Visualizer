from Model.Node import Node 
from Model.Layer import Layer

class Network():
    def __init__(self) -> None:
        self._layers = []
        self._edges = []
    
    @property
    def layers(self) -> list[Layer]:
        return self._layers
    
    @property
    def edges(self) -> list[(str, str)]:
        return self._edges

    def add_edges(self) -> None:
        numLayers = len(self._layers)
        for i in range(numLayers):
            isLastLayer = (i == (numLayers - 1))
            if isLastLayer:
                break

            self._add_edges_between_layers(i, i + 1)
    
    def _add_edges_between_layers(self, i, j) -> None:
        assert i < j, "layer 1 must be less than layer 2"
        assert i >= 0, "first layer must be greater than -1"
        assert j < len(self._layers), "second layer cannot be greater than number of total layers"

        layer1 = self._layers[i]
        layer2 = self._layers[j]
        for node1 in layer1.nodes:
            for node2 in layer2.nodes:
                self._edges.append((node1, node2))
    
    def add_layer(self, size, color) -> None:
        newNodes = [Node(color) for _ in range(size)]
        newLayer = Layer(newNodes)
        self._layers.append(newLayer)
        self.add_edges()
    
    def remove_layer(self) -> None:
        pass

    def get_node_positions(self) -> None:
        nodePos = dict()
        for layerNum, layer in enumerate(self._layers):
            nodePos.update((node, (layerNum, nodeNum)) for nodeNum, node in enumerate(layer.nodes))
        
        return nodePos
    