from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base
import uuid


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4())
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
