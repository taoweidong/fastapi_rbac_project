from infrastructure.db import SessionLocal
from schemas.role import RoleCreate


def create_role(role: RoleCreate):
    db = SessionLocal()
    # 假设我们有更多的角色逻辑
    return {"role": role}
