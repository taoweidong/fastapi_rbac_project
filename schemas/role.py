from pydantic import BaseModel

from pydantic import BaseModel, Field
from typing import Optional


class Role(BaseModel):
    name: str = Field(..., max_length=50, description="名称")
    role_key: str = Field(..., max_length=50, description="权限字符")
    data_range: int = Field(4, description="数据权限范围")
    disabled: bool = Field(False, description="是否禁用")
    order: Optional[int] = Field(None, description="排序")
    desc: Optional[str] = Field(None, max_length=255, description="描述")
    is_admin: bool = Field(False, description="是否为超级角色")


class RoleResponse(Role):
    id: int = Field(..., description="ID")

    class Config:
        orm_mode = True  # 启用 ORM 模式
