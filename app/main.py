from fastapi import FastAPI
from app.api.v1.endpoints import test_routes

app = FastAPI(title="Title tự đặt : 1Auto Web App")  # <- Biến 'app' phải tồn tại

app.include_router(test_routes.router, prefix="/api/v1/test2", tags=["Test"])


# uvicorn app.main:app --reload
