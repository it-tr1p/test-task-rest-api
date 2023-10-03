from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.db.db_url_config import Config

Base = declarative_base()

engine = create_async_engine(
    url=Config.DB_CONFIG,
    echo=True
)

async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
