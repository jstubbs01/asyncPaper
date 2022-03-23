from lib2to3.pgen2.token import OP
from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.papers import Paper

class PaperDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_paper(self, name: str, author: str,   release_year: int, url: str):
        new_paper = Paper(name=name,author=author, release_year=release_year, url=url)
        self.db_session.add(new_paper)
        await self.db_session.flush()

    async def get_all_papers(self) -> List[Paper]:
        q = await self.db_session.execute(select(Paper).order_by(Paper.id))
        return q.scalars().all()

    async def update_paper(self, paper_id: int, name: Optional[str], author: Optional[str], release_year: Optional[int], url: Optional[str]):
        q = update(Paper).where(Paper.id == paper_id)
        if name:
            q = q.values(name=name)
        if author:
            q = q.values(author=author)
        if release_year:
            q = q.values(release_year=release_year)
        if url:
            q = q.values(url=url)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)