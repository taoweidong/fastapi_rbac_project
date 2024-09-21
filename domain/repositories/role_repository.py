from sqlalchemy.orm import Session

from domain.models.user import User
from infrastructure.BaseRepository import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(db, User)
