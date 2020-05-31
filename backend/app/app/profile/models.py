from sqlalchemy import BigInteger, Column, String
from app.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    full_name = Column(String)
