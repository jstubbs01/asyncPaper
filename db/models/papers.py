from sqlalchemy import Column, Integer, String

from db.config import Base

class Paper(Base):
    __tablename__ = 'papers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    url = Column(String, nullable=False)