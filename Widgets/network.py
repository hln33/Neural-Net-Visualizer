import uuid
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Network(FigureCanvas):
    def __init__(self, graph, figure):
        super(Network, self).__init__()

        self.graph = graph
        self.figure = figure
        self.layers = []
        self._draw_network()

    def _draw_network(self):
        self._clear_network()

        self._add_nodes()
        self._add_edges()

        pos = self._get_node_positions()
        nx.draw(self.graph, pos=pos, with_labels=False)
        self.draw_idle()
    
    def _clear_network(self):
        self.figure.clf()
    
    def add_layer(self, size):
        newLayer = [self._generate_node_id() for _ in range(size)]
        self.layers.append(newLayer)
        self._draw_network()
    
    def remove_layer(self):
        pass

    def _generate_node_id(self):
        return str(uuid.uuid4())

    def _get_node_positions(self):
        pos = dict()
        for layerNum, layer in enumerate(self.layers):
            pos.update((node, (layerNum, nodeNum)) for nodeNum, node in enumerate(layer))
        
        return pos
    
    def _add_nodes(self):
        for i, layer in enumerate(self.layers):
            self.graph.add_nodes_from(layer, bipartite=i)

    def _add_edges(self):
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
        for node1 in layer1:
            for node2 in layer2:
                self.graph.add_edge(node1, node2)
            