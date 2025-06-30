from pydantic import BaseModel
from typing import Optional

class TestRequestCreate(BaseModel):
    device_id: str

class TestResult(BaseModel):
    request_id: int
    result: str


class TestRequestUpdate(BaseModel):
    result: str


class TestRequestOut(BaseModel):
    id: int
    device_id: str
    status: str
    result: Optional[str] = None

    class Config:
        orm_mode = True