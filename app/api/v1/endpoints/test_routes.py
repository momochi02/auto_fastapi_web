from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.test_schema import TestRequestCreate, TestResult
from app.services.test_service import TestService

router = APIRouter()

@router.post("/send")
def send_test(request: TestRequestCreate, db: Session = Depends(get_db)):
    return TestService(db).create_test_request(request)

@router.post("/result")
def send_result(result: TestResult, db: Session = Depends(get_db)):
    return TestService(db).save_result(result)
