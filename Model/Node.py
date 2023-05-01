import uuid

class Node():
    def __init__(self, color: str) -> None:
        self.color = color
        self.id = self._generate_id()
    
    def _generate_id(self) -> str:
        return str(uuid.uuid4())