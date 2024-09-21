#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2022/7/7 13:41
# @File           : role.py
# @IDE            : PyCharm
# @desc           : 角色模型
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.db import Base


class Role(Base):
    __tablename__ = "auth_role"
    __table_args__ = ({'comment': '角色表'})
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment='ID')
    name: Mapped[str] = mapped_column(String(50), index=True, comment="名称")
    role_key: Mapped[str] = mapped_column(String(50), index=True, comment="权限字符")
    data_range: Mapped[int] = mapped_column(Integer, default=4, comment="数据权限范围")
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否禁用")
    order: Mapped[int | None] = mapped_column(Integer, comment="排序")
    desc: Mapped[str | None] = mapped_column(String(255), comment="描述")
    is_admin: Mapped[bool] = mapped_column(Boolean, comment="是否为超级角色", default=False)
