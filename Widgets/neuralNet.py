import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from Model.Network import Network

# constants
NODE_COLOR = 'black'

class NeuralNetwork(FigureCanvas):
    def __init__(self, graph, figure):
        super().__init__()

        self.graph = graph
        self.figure = figure
        self.network = Network()

        self._draw_network()

    def _draw_network(self):
        self._clear_network()
        self._add_nodes()
        self._add_edges()

        node_positions = self.network.get_node_positions()
        color_map = self._get_node_color_map(len(node_positions))
        nx.draw(self.graph, node_color=color_map, pos=node_positions, with_labels=False)
        self.draw_idle()
    
    def _clear_network(self):
        self.figure.clf()
    
    def add_layer(self, size):
        self.network.add_layer(size, NODE_COLOR)
        self._draw_network()
    
    def remove_layer(self, i):
        pass

    def _get_node_color_map(self, num_nodes):
        color_map = []
        for _ in range(num_nodes):
            color_map.append(NODE_COLOR)
        
        return color_map
    
    def _add_nodes(self):
        for i, layer in enumerate(self.network.layers):
            self.graph.add_nodes_from(layer.nodes, bipartite=i)

    def _add_edges(self):
        for node1, node2 in self.network.edges:
            self.graph.add_edge(node1, node2)
            