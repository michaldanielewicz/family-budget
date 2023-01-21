from typing import Union

from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, user_id: int) -> Union[models.UserInfo, None]:
    return db.query(models.UserInfo).filter(models.UserInfo.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Union[models.UserInfo, None]:
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def get_all_users(db: Session) -> Union[list[models.UserInfo], None]:
    # TODO: im erasing ', skip: int = 0, limit: int = 100' part since i will be implementing pagination
    return db.query(models.UserInfo).all()


def get_filtered_users_by_username(db: Session, username: str) -> Union[list[models.UserInfo], None]:
    return db.query(models.UserInfo).filter(models.UserInfo.username.like(f"%{username}%")).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.UserInfo:
    # TODO: implement hashing password
    db_user = models.UserInfo(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
