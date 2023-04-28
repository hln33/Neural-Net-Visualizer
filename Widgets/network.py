import networkx as nx

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Network(FigureCanvas):
    def __init__(self):
        super(Network, self).__init__()

        self.graph = nx.Graph()

        self.layers = []
        self.layers.append([1, 2, 3, 4])
        self.layers.append(['a', 'b', 'c', 'd', 'e'])

        self.figure = plt.figure()
        self._plot_graph()

    def _plot_graph(self):
        self.figure.clf()
        self._add_nodes()
        self._add_edges()

        pos = self._get_node_positions()
        nx.draw(self.graph, pos=pos, with_labels=False)
        self.draw_idle()
    
    def remove_layer(self):
        pass
    
    def add_layer(self):
        pass

    def _get_node_positions(self):
        pos = dict()
        for layerNum, layer in enumerate(self.layers):
            pos.update((node, (layerNum, nodeNum)) for nodeNum, node in enumerate(layer))
        
        return pos
    
    def _add_nodes(self):
        for i, layer in enumerate(self.layers):
            self.graph.add_nodes_from(layer, bipartite=i)

    def _add_edges(self):
        for i in range(len(self.layers)):
            isLastLayer = (i == (len(self.layers) - 1))
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
            