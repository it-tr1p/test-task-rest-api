from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship

from app.db import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    time_create = Column(DateTime, nullable=False, server_default=func.now())
    time_update = Column(DateTime, nullable=True, onupdate=func.now())
    views_count = Column(Integer, nullable=False, default=0)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=True)


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    time_create = Column(DateTime, server_default=func.now())
    time_update = Column(DateTime, onupdate=func.now())

    notes = relationship("Note", backref="board", lazy="selectin")
