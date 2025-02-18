from fastapi import FastAPI
from routers import items, users  # users.py 추가

app = FastAPI()

# APIRouter 추가
app.include_router(items.router)  # 아이템 관련 API 등록
app.include_router(users.router)  # 사용자 관련 API 등록


