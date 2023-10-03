import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres1")
    DB_NAME = os.getenv("DB_NAME", "notion_api")
    DB_HOST = os.getenv("DB_HOST", "0.0.0.0")
    DB_PORT = os.getenv("DB_PORT", "5433")

    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


if __name__ == "__main__":
    print(Config.DB_CONFIG)
