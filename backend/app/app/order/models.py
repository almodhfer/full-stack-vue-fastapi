from app.db.base import Base
from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.profile import User


class Order(Base):
    __tablename__ = 'orders'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey(User.id))
    user = relationship(User)
