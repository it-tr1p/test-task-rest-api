from app.schemas.notes import NoteModelText
from app.utils.unitofwork import IUnitOfWork


class NotesService:
    async def add_note(self, uow: IUnitOfWork, note: NoteModelText):
        async with uow:
            notes_dict = note.model_dump()
            note_id = await uow.notes.add_one(notes_dict)
            await uow.commit()
            return note_id

    async def get_all_notes(self, uow: IUnitOfWork):
        async with uow:
            notes = await uow.notes.find_all()
            return notes

    async def get_note(self, uow: IUnitOfWork, note_id):
        async with uow:
            curr_note = await uow.notes.find_one(id=note_id)
            curr_note.views_count += 1
            await uow.notes.edit_one(note_id=curr_note.id, data=curr_note.dict())
            await uow.commit()
            return curr_note

    async def edit_note(self, uow: IUnitOfWork, note_id: int, note: NoteModelText):
        data = note.model_dump()
        async with uow:
            await uow.notes.edit_one(note_id, data)
            await uow.commit()

    async def delete_note(self, uow: IUnitOfWork, note_id):
        async with uow:
            result = await uow.notes.delete(note_id)
            await uow.commit()
            return {"Deleted": result}

    #
    #
    # async def get_one(self, note_id: int):
    #     curr_note = await self.notes_repo.find_one(note_id)
    #     return curr_note
    #
    #
    # async def delete_note(self, note_id):
    #     result = await self.notes_repo.delete(note_id)
    #     return {"Deleted": result}

# class NotesService:
#     def __init__(self, notes_repo: AbstractRepository):
#         self.notes_repo: AbstractRepository = notes_repo()
#
#     async def add_note(self, note: NoteModelAdd):
#         notes_dict = note.model_dump()
#         note_id = await self.notes_repo.add_one(notes_dict)
#         return note_id
#
#     async def get_notes(self):
#         notes = await self.notes_repo.find_all()
#         return notes
#
#     async def get_one(self, note_id: int):
#         curr_note = await self.notes_repo.find_one(note_id)
#         return curr_note
#
#     async def edit_note(self, note_id: int, note: NoteModelAdd):
#         notes_dict = note.model_dump()
#         await self.notes_repo.edit_one(note_id, notes_dict)
#         return {}
#
#     async def delete_note(self, note_id):
#         result = await self.notes_repo.delete(note_id)
#         return {"Deleted": result}
#
