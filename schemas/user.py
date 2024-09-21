from pydantic import BaseModel, constr, EmailStr
from typing import Optional
from datetime import datetime


# 基本的公共用户模型
class User(BaseModel):
    avatar: Optional[str]
    telephone: constr(min_length=11, max_length=11)  # 电话号码为 11 位
    email: Optional[EmailStr]
    name: constr(max_length=50)
    nickname: Optional[str]
    gender: Optional[str]
    is_active: Optional[bool] = True
    is_reset_password: Optional[bool] = False
    last_ip: Optional[str]
    last_login: Optional[datetime]
    is_staff: Optional[bool] = False


# 用于创建用户时的模型，包含密码字段
class UserCreate(User):
    password: constr(min_length=8, max_length=255)


# 用于更新用户时的模型，所有字段都是可选的
class UserUpdate(BaseModel):
    avatar: Optional[str]
    telephone: Optional[constr(min_length=11, max_length=11)]
    email: Optional[EmailStr]
    name: Optional[constr(max_length=50)]
    nickname: Optional[str]
    password: Optional[constr(min_length=8, max_length=255)]
    gender: Optional[str]
    is_active: Optional[bool]
    is_reset_password: Optional[bool]
    last_ip: Optional[str]
    last_login: Optional[datetime]
    is_staff: Optional[bool]


# 用于响应的模型，包含 id 字段，隐藏密码字段
class UserResponse(User):
    id: int

    class Config:
        orm_mode = True
