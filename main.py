from typing import List

import uvicorn
from fastapi import FastAPI

from db.config import engine, Base, asyncSession
from db.data_accs.paper_dataccs import PaperDAL
from db.models.papers import Paper

app = FastAPI()


@app.get("/papers")
async def create_paper(name: str, author: str, release_year: int, url: str):
    async with asyncSession() as session:
        async with session.begin():
            paper_dat_accs = PaperDAL(session)
            return await PaperDAL.create_book(name, author, release_year)

if __name__ == '__main__' :
   uvicorn.run("app:app", port=8000, host='127.0.0.1')
