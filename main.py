from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.rbac import router  # 假设你的路由在 app/api.py 中

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

# 注册路由
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=9999)
