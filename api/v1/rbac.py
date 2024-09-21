from fastapi import APIRouter
from schemas.user import UserCreate
from schemas.role import RoleCreate
from services.user_service import create_user
from services.role_service import create_role

router = APIRouter()


@router.post("/users/")
def create_new_user(user: UserCreate):
    return create_user(user)


@router.post("/roles/")
def create_new_role(role: RoleCreate):
    return create_role(role)
