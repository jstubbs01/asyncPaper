import uvicorn
from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__' :
   uvicorn.run("app:app", port=8000, host='127.0.0.1')
