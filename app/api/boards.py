from http import HTTPStatus

from fastapi import APIRouter

from app.schemas import BoardModelName
from app.services.boards import BoardsService
from app.api.dependencies import UOWDep

router = APIRouter()


@router.get("/{board_id}")
async def get_one_board(
        board_id: int,
        uow: UOWDep,
        # board: boardModelText,
):
    board = await BoardsService().get_board(uow, board_id)
    return board


@router.post("/", status_code=HTTPStatus.CREATED)
async def add_board(
        board: BoardModelName,
        uow: UOWDep,
):
    board_id = await BoardsService().add_board(uow, board)
    return {"board_id": board_id}


@router.post("/add/{board_id}/{note_id}")
async def add_note_to_board(
        board_id: int,
        note_id: int,
        uow: UOWDep,
):
    board = await BoardsService().add_note_to_board(uow, board_id, note_id)
    return board


@router.patch("/remove/{note_id}")
async def remove_note_from_board(
        note_id: int,
        uow: UOWDep,
):
    board = await BoardsService().remove_note_from_board(uow, note_id)
    return board


@router.patch("/{board_id}")
async def edit_board(
        board_id: int,
        board: BoardModelName,
        uow: UOWDep,
):
    await BoardsService().edit_board(uow, board_id, board)
    return {"Ok": True}


@router.get("/")
async def get_all_boards(
        uow: UOWDep,
):
    boards = await BoardsService().get_all_boards(uow)
    return boards


@router.delete("/{board_id}")
async def delete(
        board_id: int,
        uow: UOWDep,
):
    boards = await BoardsService().delete_board(uow, board_id)
    return boards
