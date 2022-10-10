from dataclasses import dataclass

__all__ = [
    "Message"
]

@dataclass
class Message:
    created_at: str
    id: str
    text: str
    updated_at: str
