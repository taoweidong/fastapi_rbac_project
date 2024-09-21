from infrastructure.db import SessionLocal
from schemas.role import Role


def create_role(role: Role):
    db = SessionLocal()
    # 假设我们有更多的角色逻辑
    return {"role": role}
