from Model.Node import Node

class Layer():
    def __init__(self, nodes: list[Node]) -> None:
        self._nodes = nodes
    
    @property
    def nodes(self) -> list[Node]:
        return self._nodes