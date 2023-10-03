from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.utils.repository import SQLAlchemyRepository
from app.db.models import Board, Note
from app.schemas import BoardSchema


class BoardsRepository(SQLAlchemyRepository):
    model = Board
    pydantic_model = BoardSchema

    async def add_note_to_board(self, note_id):
        stmt = (
            select(Note)
            .where(Note.id == note_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar()

    async def remove_note_from_board(self, note_id):
        stmt = (
            select(Note)
            .where(Note.id == note_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar()

    async def get_all_boards_with_notes(self):
        session = self.session
        stmt = (
            select(Board)
            .outerjoin(Note, Board.id == Note.board_id)
            .options(selectinload(Board.notes))
            .distinct()
        )
        result = await session.execute(stmt)
        boards = result.scalars().all()
        board_dicts = []
        for board in boards:
            board_dict = {
                "id": board.id,
                "name": board.name,
                "time_create": board.time_create,
                "time_update": board.time_update,
                "notes": []
            }
            for note in board.notes:
                note_dict = {
                    "id": note.id,
                    "text": note.text,
                    "board_id": note.board_id
                }
                board_dict["notes"].append(note_dict)
            board_dicts.append(board_dict)
        return board_dicts

    async def get_one_board(self, board_id: int):
        stmt = (
            select(Board)
            .where(Board.id == board_id)
            .options(selectinload(Board.notes))  # Загружаем связанные записи
        )
        result = await self.session.execute(stmt)
        board = result.scalar()
        if not board:
            return {"None": False}
        board_dict = {
            "id": board.id,
            "name": board.name,
            "time_create": board.time_create,
            "time_update": board.time_update,
            "notes": []
        }

        for note in board.notes:
            note_dict = {
                "id": note.id,
                "text": note.text,
                "board_id": note.board_id
            }
            board_dict["notes"].append(note_dict)

        return board_dict
