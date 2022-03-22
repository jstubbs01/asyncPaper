from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.papers import Paper

class PaperDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_paper(self, name: str, author: str, release_year: int, url: str):
        new_paper = Paper(name=name,author=author, release_year=release_year, url=url)
        self.db_session.add(new_paper)
        await self.db_session.flush()

    async def get_evry_paper(self) -> List[Paper]:
    x = await self.db_session.execute(select(Paper).order_by(Paper.id))
        return x.scalars().all()

    async def update_paper(self, paper_id: int, name: Optional[str], author: Optional[str], 
    release_year: Optional[int], url: [str]):
        x = update(Paper).where(Paper.id == paper_id)
        if name:
            x = x.values(name=name)
        if author:
            x = x.values(author=author)
        if release_year:
            x = x.values(release_year=release_year)
        x.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(x)