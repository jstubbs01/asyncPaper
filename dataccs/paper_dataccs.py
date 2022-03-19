from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.papers import Paper

class PaperDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_paper(self, name: str, author: str,   release_year: int):
        new_paper = Paper(name=name,author=author, release_year=release_year)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_all_papers(self) -> List[Paper]:
        q = await self.db_session.execute(select(Paper).order_by(Paper.id))
        return q.scalars().all()

    async def update_paper(self, paper_id: int, name: Optional[str], author: Optional[str], release_year: Optional[int]):
        q = update(Paper).where(Paper.id == paper_id)
        if name:
            q = q.values(name=name)
        if author:
            q = q.values(author=author)
        if release_year:
            q = q.values(release_year=release_year)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)