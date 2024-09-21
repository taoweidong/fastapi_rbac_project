#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2022/7/7 13:41
# @File           : user_api.py
# @IDE            : PyCharm
# @desc           : 用户模型

from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.db import Base

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class User(Base):
    __tablename__ = "auth_user"
    __table_args__ = ({'comment': '用户表'})
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment='用户ID')
    avatar: Mapped[str | None] = mapped_column(String(500), comment='头像')
    telephone: Mapped[str] = mapped_column(String(11), nullable=False, index=True, comment="手机号", unique=False)
    email: Mapped[str | None] = mapped_column(String(50), comment="邮箱地址")
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="姓名")
    nickname: Mapped[str | None] = mapped_column(String(50), nullable=True, comment="昵称")
    password: Mapped[str] = mapped_column(String(255), nullable=True, comment="密码")
    gender: Mapped[str | None] = mapped_column(String(8), nullable=True, comment="性别")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, comment="是否可用")
    is_reset_password: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        comment="是否已经重置密码，没有重置的，登陆系统后必须重置密码"
    )
    last_ip: Mapped[str | None] = mapped_column(String(50), comment="最后一次登录IP")
    last_login: Mapped[datetime | None] = mapped_column(DateTime, comment="最近一次登录时间")
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否为工作人员")
