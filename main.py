from typing import List, Optional

import uvicorn
from fastapi import FastAPI

from db.config import engine, Base, async_session
from db.data_accs.paper_dataccs import PaperDAL
from db.models.papers import Paper

app = FastAPI()
app.include_router(paper_router.router)

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.post("/papers")
async def create_paper(name: str, author: str, release_year: int, url: str):
    async with async_session() as session:
        async with session.begin():
            paper_dal = PaperDAL(session)
            return await paper_dal.create_paper(name, author, release_year, url)


@app.get("/papers")
async def get_all_papers() -> List[Paper]:
    async with async_session() as session:
        async with session.begin():
            paper_dal = PaperDAL(session)
            return await paper_dal.get_all_papers()

@app.put("/papers/{paper_id}")
async def update_paper(paper_id: int, name: Optional[str] = None, author: Optional[str] = None, release_year: Optional[int] = None, url: Optional[str]=None):
    async with async_session() as session:
        async with session.begin():
            paper_dal = PaperDAL(session)
            return await paper_dal.update_paper(paper_id, name, author, release_year, url)


if __name__ == '__main__':
    uvicorn.run("app:app", port=1111, host='127.0.0.1')
