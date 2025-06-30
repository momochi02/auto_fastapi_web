from app.db.session import engine
from app.db.models import Base

print("🔧 Creating database...")
Base.metadata.create_all(bind=engine)
print("✅ Done!")

from sqlalchemy import inspect
inspector = inspect(engine)
tables = inspector.get_table_names()
print("📦 Các bảng trong database:")
for table in tables:
    print(f" - {table}")


print("📄 Các bảng được định nghĩa từ Base:")
for table in Base.metadata.tables:
    print(f" - {table}")