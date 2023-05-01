from Model.Node import Node 
from Model.Layer import Layer

class Network():
    def __init__(self):
        self.layers = []
        self.edges = []

    def add_edges(self):
        numLayers = len(self.layers)
        for i in range(numLayers):
            isLastLayer = (i == (numLayers - 1))
            if isLastLayer:
                break

            self._add_edges_between_layers(i, i + 1)
    
    def _add_edges_between_layers(self, i, j):
        assert i < j, "layer 1 must be less than layer 2"
        assert i >= 0, "first layer must be greater than -1"
        assert j < len(self.layers), "second layer cannot be greater than number of total layers"

        layer1 = self.layers[i]
        layer2 = self.layers[j]
        for node1 in layer1.nodes:
            for node2 in layer2.nodes:
                self.edges.append((node1, node2))
    
    def add_layer(self, size, color):
        newNodes = [Node(color) for _ in range(size)]
        newLayer = Layer(newNodes)
        self.layers.append(newLayer)
        self.add_edges()
    
    def remove_layer(self):
        pass

    def get_node_positions(self):
        nodePos = dict()
        for layerNum, layer in enumerate(self.layers):
            nodePos.update((node, (layerNum, nodeNum)) for nodeNum, node in enumerate(layer.nodes))
        
        return nodePos
    