import uvicorn
from fastapi import FastAPI

from app.api.notes import router as notes_router
from app.api.boards import router as boards_router


app = FastAPI(
    title="Notes API",
    description="Test task",
    docs_url="/"
)

app.include_router(notes_router, prefix="/notes", tags=["notes"])
app.include_router(boards_router, prefix="/boards", tags=["boards"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
