from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base

class TestRequest(Base):
    __tablename__ = "test_requests"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(50))
    status = Column(String(20), default="pending")
    result = Column(Text, nullable=True)
