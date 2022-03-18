from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

url = "sqlite+aoisqlite:///./test.db"

# make async engine at url, see output

engine = create_async_engine(url, future=True, echo=True)

# make asychronous session for db, witj entities and fields 
# available even after a commit
asyncSesh=sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base=declarative_base()