import os


class Settings:
    PROJECT_NAME: str = "FastAPI RBAC"
    # 获取项目根目录的绝对路径
    BASE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 构造数据库连接 URL
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_ROOT, 'db', 'test.db')}"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
