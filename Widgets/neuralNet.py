from Model.network import Network

import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# constants
NODE_COLOR = 'black'

class NeuralNetwork(FigureCanvas):
    def __init__(self, graph: nx.Graph, figure: Figure, model: Network) -> None:
        super().__init__()
        
        self.graph = graph
        self.figure = figure
        self.model = model

        self._draw_network()

    def _draw_network(self) -> None:
        self._clear_network()
        self._add_nodes()
        self._add_edges()

        node_positions = self.model.get_node_positions()
        color_map = self._get_node_color_map()
        nx.draw(self.graph, node_color=color_map, pos=node_positions, with_labels=False)
        self.draw_idle()
    
    def _clear_network(self) -> None:
        self.figure.clf()
    
    def add_layer(self, size) -> None:
        self.model.add_layer(size, NODE_COLOR)        
        self._draw_network()
    
    def remove_layer(self, i) -> None:
        pass

    def _get_node_color_map(self) -> list[str]:
        color_map = []
        for layer in self.model.layers:
            for node in layer.nodes:
                color_map.append(node.color)
        
        return color_map
    
    def _add_nodes(self) -> None:
        layers = self.model.layers

        for i, layer in enumerate(layers):
            self.graph.add_nodes_from(layer.nodes, bipartite=i)

    def _add_edges(self) -> None:
        edges = self.model.edges
        
        for node1, node2 in edges:
            self.graph.add_edge(node1, node2)
            