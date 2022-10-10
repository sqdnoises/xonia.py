from dataclasses import dataclass

from . import Message

__all__ = [
    "Channel"
]

class Channel:
    """Represents a channel."""

    messages: list[Message]

    def find_message(self, id: str) -> Message:
        """Find a message given the ID."""
        return [m for m in self.messages if m.id == id][0]
