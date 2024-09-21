```bash
fastapi_rbac/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 应用的入口
│   ├── api/             # 接口层
│   │   ├── __init__.py
│   │   ├── v1/          # API 版本控制
│   │   │   ├── __init__.py
│   │   │   ├── rbac.py  # RBAC相关的API
│   ├── core/            # 核心配置和依赖
│   │   ├── __init__.py
│   │   ├── config.py    # 项目的配置文件
│   │   ├── security.py  # 权限、加密相关工具
│   ├── domain/          # 领域层
│   │   ├── __init__.py
│   │   ├── models/      # 领域模型
│   │   │   ├── __init__.py
│   │   │   ├── user.py  # 用户模型
│   │   │   ├── role.py  # 角色模型
│   │   ├── repositories/ # 仓储层，负责与数据库的交互
│   │       ├── __init__.py
│   │       ├── user_repository.py
│   │       ├── role_repository.py
│   ├── infrastructure/  # 基础设施层
│   │   ├── __init__.py
│   │   ├── db.py        # 数据库连接设置
│   │   ├── migrations/  # 数据库迁移
│   │   │   ├── __init__.py
│   │   │   ├── versions/
│   ├── schemas/         # 数据传输对象（DTO）
│   │   ├── __init__.py
│   │   ├── user.py      # 用户相关的请求/响应模型
│   │   ├── role.py      # 角色相关的请求/响应模型
│   ├── services/        # 应用服务层
│   │   ├── __init__.py
│   │   ├── user_service.py  # 用户相关业务逻辑
│   │   ├── role_service.py  # 角色相关业务逻辑
│   ├── tests/           # 测试代码
│   │   ├── __init__.py
│   │   ├── test_rbac.py
│   └── utils/           # 通用工具类
│       ├── __init__.py
│       ├── hashing.py   # 密码哈希工具
│       ├── jwt.py       # JWT 生成与验证
├── requirements.txt     # 项目依赖列表
├── alembic.ini          # Alembic 数据库迁移工具配置
├── Dockerfile           # Docker 容器配置
├── docker-compose.yml   # Docker 容器编排配置
├── README.md            # 项目说明


```