# -*- coding: utf-8 -*-
from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session

# 定义类型变量
ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType]):
    def __init__(self, db: Session, model: ModelType):
        self.db = db
        self.model = model

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, obj_id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == obj_id).first()

    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()

    def update(self, obj: ModelType) -> ModelType:
        existing_obj = self.db.query(self.model).filter(self.model.id == obj.id).first()
        if existing_obj:
            for key, value in obj.__dict__.items():
                setattr(existing_obj, key, value)
            self.db.commit()
            self.db.refresh(existing_obj)
            return existing_obj
        return None

    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.commit()

    def bulk_delete(self, ids: List[int]) -> None:
        self.db.query(self.model).filter(self.model.id.in_(ids)).delete(synchronize_session=False)
        self.db.commit()
