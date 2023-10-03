from http import HTTPStatus

from fastapi import APIRouter

from app.schemas.notes import NotedAdd, NoteModelText
from app.services.notes import NotesService
from app.api.dependencies import UOWDep

router = APIRouter()


@router.get("/{note_id}")
async def get_one_note(
        note_id: int,
        uow: UOWDep,
        # note: NoteModelText,
):
    notes = await NotesService().get_note(uow, note_id)
    return notes


@router.post("/", status_code=HTTPStatus.CREATED)
async def add_note(
        note: NotedAdd,
        uow: UOWDep,
):
    note_id = await NotesService().add_note(uow, note)
    return {"note_id": note_id}


@router.patch("/{note_id}")
async def edit_note(
        note_id: int,
        note: NoteModelText,
        uow: UOWDep,
):
    await NotesService().edit_note(uow, note_id, note)
    return {"Ok": True}


@router.get("/")
async def get_all_notes(
        uow: UOWDep,
):
    notes = await NotesService().get_all_notes(uow)
    return notes


@router.delete("/{note_id}")
async def delete(
        note_id: int,
        uow: UOWDep,
):
    notes = await NotesService().delete_note(uow, note_id)
    return notes
