from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.request import TestRequestCreate, TestRequestUpdate, TestRequestOut,TestResult
from app.services.test_service import TestService
from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()

# @router.post("/send")
# def send_test(request: TestRequestCreate, db: Session = Depends(get_db)):
#     return TestService(db).create_test_request(request)
#
# @router.post("/result")
# def send_result(result: TestResult, db: Session = Depends(get_db)):
#     return TestService(db).save_result(result)
#
#
@router.post("/get-all", response_model=list[TestRequestOut])
def get_all_requests(db: Session = Depends(get_db)):
    return TestService(db).get_all()



# @router.put("/{id}", response_model=TestRequestOut)
# def update(id: int, request: TestRequestUpdate, db: Session = Depends(get_db)):
#     result = TestService(db).update(id, request)
#     if not result:
#         raise HTTPException(status_code=404, detail="Not found")
#     return result
#
# @router.delete("/{id}")
# def delete(id: int, db: Session = Depends(get_db)):
#     success = TestService(db).delete(id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Not found")
#     return {"ok": True}
#
# # ✅ Bổ sung thêm hàm POST mới - tạo device test với status tùy chọn
# @router.post("/custom", response_model=TestRequestOut)
# def create_with_status(device_id: str, status: str = "pending", db: Session = Depends(get_db)):
#     # Bạn có thể custom thêm xử lý tại đây
#     item = TestService(db).repo.create(device_id)
#     item.status = status
#     db.commit()
#     db.refresh(item)
#     return item
#
# # ✅ Bổ sung thêm hàm PUT - cập nhật status riêng
# @router.put("/{id}/status")
# def update_status(id: int, status: str, db: Session = Depends(get_db)):
#     item = db.query(TestService(db).repo.model).get(id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Not found")
#     item.status = status
#     db.commit()
#     return {"ok": True, "new_status": status}
#
# # ✅ Bổ sung thêm hàm DELETE ALL
# @router.delete("/")
# def delete_all(db: Session = Depends(get_db)):
#     items = TestService(db).get_all()
#     for item in items:
#         db.delete(item)
#     db.commit()
#     return {"ok": True, "deleted": len(items)}