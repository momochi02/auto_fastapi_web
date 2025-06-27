from fastapi import FastAPI
from api.v1.endpoints import test_routes

app = FastAPI(title="Auto Web App")

# Đăng ký router
app.include_router(test_routes.router, prefix="/api/v1/test", tags=["Test"])
