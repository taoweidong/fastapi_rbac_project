from typing import List

from fastapi import Depends, APIRouter
from fastapi import HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session

from domain.repositories.role_repository import UserRepository
from infrastructure.db import get_db
from schemas.user import User, UserResponse

user_router = APIRouter()


@user_router.get("/users/paginated/", tags=["User"], response_model=List[UserResponse])
def get_paginated_users(
        limit: int = Query(10, ge=1),  # 默认每页返回 10 条记录
        offset: int = Query(0, ge=0),  # 默认从第 0 条记录开始
        db: Session = Depends(get_db)
):
    # users = db.query(User).offset(offset).limit(limit).all()

    # 初始化 UserRepository 实例
    user_repository = UserRepository(db)

    # 调用 get_all 方法
    users = user_repository.get_all()

    print(len(users))

    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
