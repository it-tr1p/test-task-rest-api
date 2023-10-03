from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from app.schemas import NoteSchema


class BoardModelName(BaseModel):
    name: str


class BoardSchema(BaseModel):
    id: int
    name: str
    time_create: datetime
    time_update: Optional[datetime] = None

    notes: List[NoteSchema] = Field(default_factory=list)

    class Config:
        from_attributes = True


