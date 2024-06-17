from typing import TypedDict
from datetime import datetime


class Todo(TypedDict):
    id: int
    title: str
    description: str
    priority: int
    updated_at: datetime
