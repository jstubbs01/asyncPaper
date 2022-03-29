from typing import List, Optional

from fastapi import APIRouter

from db.config import async_session
from db.data_accs.paper_dataccs import PaperDAL
from db.models.papers import Paper
from dependencies import getPaperDal

router = APIRouter()


@router.post("/papers")
async def create_paper(name: str, author: str, release_year: int, url: str):
    return await paper_dal.create_paper(name, author, release_year, url)


@router.get("/papers")
async def get_all_papers() -> List[Paper]:
    return await paper_dal.get_all_papers()

@router.put("/papers/{paper_id}")
async def update_paper(paper_id: int, name: Optional[str] = None, author: Optional[str] = None, release_year: Optional[int] = None, url: Optional[str]=None):
    return await paper_dal.update_paper(paper_id, name, author, release_year, url)