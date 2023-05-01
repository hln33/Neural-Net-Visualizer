import uuid

class Node():
    def __init__(self, color):
        self.color = color
        self.id = self._generate_id()
    
    def _generate_id(self):
        return str(uuid.uuid4())