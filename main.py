import uvicorn
from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI()


@app.get("/papers")
async def root():
    return {"message": "Hello World"}

@app.post("/papers")
async def create_book(name: str, author: str, release_year: int, url: url):
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.create_book(name, author, release_year)

if __name__ == '__main__' :
   uvicorn.run("app:app", port=8000, host='127.0.0.1')
