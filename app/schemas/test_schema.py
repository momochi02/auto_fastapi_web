from pydantic import BaseModel

class TestRequestCreate(BaseModel):
    device_id: str

class TestResult(BaseModel):
    request_id: int
    result: str
