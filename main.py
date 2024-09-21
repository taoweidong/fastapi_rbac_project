from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

from api.v1.role_api import role_router
from api.v1.user_api import user_router
from schemas.role import Role
from schemas.user import User, UserCreate

app = FastAPI(
    title="FastAPI",
    description="This is a sample API",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI 文档路径
    redoc_url="/redoc",  # ReDoc 文档路径
    openapi_url="/openapi.json"  # OpenAPI 文档路径
)

# 中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(role_router)
# 注册路由
app.include_router(CRUDRouter(schema=User, create_schema=UserCreate))
app.include_router(CRUDRouter(schema=Role))


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=9999)
