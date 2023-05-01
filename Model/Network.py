
class Network():
    def __init__(self):
        self.nodes = []
        self.layers = []
    
    def add_edges(self):
        pass
    
    def add_layer(self, size):
        pass
    
    def remove_layer(self):
        pass

    def get_node_positions(self):
        nodePos = dict()
        for layerNum, layer in enumerate(self.layers):
            nodePos.update((node, (layerNum, nodeNum)) for nodeNum, node in enumerate(layer))
        
        return nodePos
    