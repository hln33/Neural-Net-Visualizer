from typing import Callable

class Observerable:
    def __init__(self) -> None:
        self.callbacks = []
    
    def register(self, c: Callable[[None], None]) -> None:
        self.callbacks.append(c)
    
    def update(self, event: dict) -> None:
        for c in self.callbacks:
            c(event)