import json
from dataclasses import dataclass

@dataclass
class Context:
    """Holds the context for the SDK"""
    data: dict

class SaaSSentinel:
    """The SDK for integrating with the memory layer"""
    def __init__(self):
        """Initialize the SDK"""
        self.context = None

    def init(self):
        """Initialize the SDK"""
        self.context = Context({})

    def setContext(self, data: dict):
        """Set the context for the SDK"""
        self.context = Context(data)

    def getContext(self) -> dict:
        """Get the context for the SDK"""
        if self.context is None:
            raise ValueError("Context not initialized")
        return self.context.data

    def to_json(self):
        """Convert the context to JSON"""
        return json.dumps(self.context.data)
