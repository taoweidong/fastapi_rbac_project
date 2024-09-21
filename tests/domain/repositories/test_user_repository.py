# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from domain.models.user import User
from domain.repositories.role_repository import UserRepository
from infrastructure.BaseRepository import BaseRepository
from infrastructure.db import get_db


class UserTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_user_repository_init(self):
        # 初始化 UserRepository 实例
        user_repository = UserRepository(get_db())

        # 验证是否正确初始化了基类
        assert isinstance(user_repository, BaseRepository)

        # 验证是否正确指定了模型
        assert user_repository.model == User

    def test_user_repository_query(self):
        # 创建一个模拟的数据库会话
        mock_db = MagicMock(spec=Session)

        # 模拟查询结果
        mock_users = [User(id=1, name="user1"), User(id=2, name="user2")]
        mock_db.query.return_value.all.return_value = mock_users

        # 初始化 UserRepository 实例
        user_repository = UserRepository(mock_db)

        # 调用 get_all 方法
        users = user_repository.get_all()

        # 验证查询方法是否被调用
        mock_db.query.assert_called_once_with(User)
        mock_db.query.return_value.all.assert_called_once()

        # 验证查询结果
        assert len(users) == 2
        assert users[0].id == 1
        assert users[0].name == "user1"
        assert users[1].id == 2
        assert users[1].name == "user2"
