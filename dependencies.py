from db.config import async_session
from db.data_accs.paper_dataccs import PaperDAL

async def getPaperDal():
    async with async_session() as session:
        async with session.begin():
            yield PaperDAL(session)