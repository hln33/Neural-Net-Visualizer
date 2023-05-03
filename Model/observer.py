from typing import Callable

class Observerable:
    def __init__(self) -> None:
        self.listener_callback = {}
    
    def register(self, listener, callback: Callable[[None], None]) -> None:
        self.listener_callback[listener] = callback
    
    def update(self, event: dict) -> None:
        for listener, callback in self.listener_callback.items():
            callback(event)