from app.utils.repository import SQLAlchemyRepository
from app.db.models import Note
from app.schemas import NoteSchema


class NotesRepository(SQLAlchemyRepository):
    model = Note
    pydantic_model = NoteSchema
