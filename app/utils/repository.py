from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import NoteSchema


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    pydantic_model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def edit_one(self, note_id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=note_id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        result = self.pydantic_model.model_validate(res.scalar_one())
        return result

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        result = [self.pydantic_model.model_validate(row) for row in result.scalars().all()]
        return result

    async def delete(self, note_id: int):
        stmt = delete(self.model).where(self.model.id == note_id)
        result = await self.session.execute(stmt)
        return result.rowcount
