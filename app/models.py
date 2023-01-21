from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base


class UserInfo(Base):
    __tablename__ = "users_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
