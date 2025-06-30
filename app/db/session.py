from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Giup biet db có những bảng

# Hàm cung cấp session cho route hoặc service
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()