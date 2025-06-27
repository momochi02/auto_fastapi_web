from app.db.repository import TestRepository
from app.schemas.test_schema import TestRequestCreate, TestResult

class TestService:
    def __init__(self, db):
        self.repo = TestRepository(db)

    def create_test_request(self, request: TestRequestCreate):
        return self.repo.create(device_id=request.device_id)

    def save_result(self, result: TestResult):
        return self.repo.update_result(request_id=result.request_id, result=result.result)
