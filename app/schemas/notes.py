from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: int
    text: str
    time_create: datetime
    time_update: Optional[datetime]
    views_count: int
    board_id: Optional[int] = None

    class Config:
        from_attributes = True



class NoteModelText(BaseModel):
    text: str


class NoteModelGet(BaseModel):
    id: int
    text: Optional[str] = None
    views_count: Optional[int] = None


class NotedAdd(BaseModel):
    text: str
    board_id: Optional[int] = None
