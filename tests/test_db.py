# -*- coding: utf-8 -*-
from domain.models.role import Role
from domain.models.user import User
from infrastructure.db import Base, engine


def create_tables():
    print(User)
    print(Role)
    """创建所有定义的表。"""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_tables()
