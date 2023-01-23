from typing import Union

from sqlalchemy.orm import Session

from app.utils import get_password_hash

from . import models, schemas


def get_user_by_id(db: Session, user_id: int) -> Union[models.UserInfo, None]:
    return db.query(models.UserInfo).filter(models.UserInfo.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Union[models.UserInfo, None]:
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def get_all_users(db: Session) -> Union[list[models.UserInfo], None]:
    return db.query(models.UserInfo).all()


def get_filtered_users_by_username(db: Session, username: str) -> Union[list[models.UserInfo], None]:
    return db.query(models.UserInfo).filter(models.UserInfo.username.like(f"%{username}%")).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.UserInfo:
    db_user = models.UserInfo(username=user.username, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_budgets(db: Session) -> Union[list[models.Budget], None]:
    return db.query(models.Budget).all()


def get_budget_by_id(db: Session, budget_id: int) -> Union[models.Budget, None]:
    return db.query(models.Budget).filter(models.Budget.id == budget_id).first()


def get_budgets_by_owner_id(db: Session, owner_id: int) -> Union[list[models.Budget], None]:
    return db.query(models.Budget).filter(models.Budget.owner_id == owner_id).all()


def create_budget(db: Session, budget: schemas.BudgetCreate, owner_id: int) -> models.Budget:
    db_budget = models.Budget(**budget.dict(), owner_id=owner_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget


def add_users_to_budget(db: Session, budget_id: int) -> models.Budget:
    db_budget = get_budget_by_id(db, budget_id)

    # do something

    db.commit()
    db.refresh(db_budget)
    return db_budget
