from pydantic import BaseModel
from typing import Optional

class TestDeviceCreate(BaseModel):
    device_id: str
class TesDeviceOut(BaseModel):
    id: int
    device_id: str
    device_name: str
    status: str
    result: Optional[str] = None
    class Config:
        orm_mode = True