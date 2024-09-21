from fastapi import APIRouter

from schemas.role import Role
from services.role_service import create_role

role_router = APIRouter()


@role_router.post("/roles/", tags=["Role"], summary="创建角色接口", description="创建角色")
def create_new_role(role: Role):
    return create_role(role)
