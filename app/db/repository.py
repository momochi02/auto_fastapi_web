from app.db.models import TestRequest

class TestRepository:
    def __init__(self, db):
        self.db = db

    def create(self, device_id: str):
        new = TestRequest(device_id=device_id, status="pending")
        self.db.add(new)
        self.db.commit()
        self.db.refresh(new)
        return new

    def update_result(self, request_id: int, result: str):
        req = self.db.query(TestRequest).get(request_id)
        if req:
            req.status = "done"
            req.result = result
            self.db.commit()
            self.db.refresh(req)
        return req
