from typing import List

from fastapi import APIRouter

from db.config import async_session
from db.data_accs.paper_dataccs import PaperDAL
from db.models.papers import Paper

router = APIRouter()


@router.post("/papers")
async def create_book(name: str, author: str, release_year: int):
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.create_book(name, author, release_year)


@router.get("/books")
async def get_all_books() -> List[Book]:
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.get_all_books()

        
@router.put("/books/{book_id}")
async def update_book(book_id: int, name: Optional[str] = None, author: Optional[str] = None, release_year: Optional[int] = None):
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.update_book(book_id, name, author, release_year)