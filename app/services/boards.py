from app.schemas import BoardModelName
from app.utils.unitofwork import IUnitOfWork


class BoardsService:
    async def add_board(self, uow: IUnitOfWork, board: BoardModelName):
        async with uow:
            boards_dict = board.model_dump()
            board_id = await uow.boards.add_one(boards_dict)
            await uow.commit()
            return board_id

    async def get_all_boards(self, uow: IUnitOfWork):
        async with uow:
            boards = await uow.boards.find_all()
            return boards

    async def get_board(self, uow: IUnitOfWork, board_id):
        async with uow:
            curr_board = await uow.boards.find_one(id=board_id)
            await uow.commit()
            return curr_board

    async def edit_board(self, uow: IUnitOfWork, board_id: int, board: BoardModelName):
        data = board.model_dump()
        async with uow:
            await uow.boards.edit_one(board_id, data)
            await uow.commit()

    async def delete_board(self, uow: IUnitOfWork, board_id):
        async with uow:
            result = await uow.boards.delete(board_id)
            await uow.commit()
            return {"Deleted": result}

    async def add_note_to_board(self, uow: IUnitOfWork, board_id, note_id):
        async with uow:
            note = await uow.boards.add_note_to_board(note_id=note_id)
            note.board_id = board_id
            await uow.commit()
            return {"Success": True}

    async def remove_note_from_board(self, uow: IUnitOfWork, note_id):
        async with uow:
            note = await uow.boards.add_note_to_board(note_id=note_id)
            note.board_id = None
            await uow.commit()
            return {"Success": True}
