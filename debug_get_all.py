from app.db.session import SessionLocal
from app.db.repository import TestRepository

db = SessionLocal()
# db.query(''__tablename__ = "test_requests"
#     id = Column(Integer, primary_key=True, index=True)
#     device_id = Column(String(50))
#     status = Column(String(20), default="pending")
#     result = Column(Text, nullable=True)''
# ).all()
repo = TestRepository(db)
data = repo.get_all()
print("✅ Dữ liệu có trong DB:")
for row in data:
    print(f"ID: {row.id}, Device: {row.device_id}, Status: {row.status}")
