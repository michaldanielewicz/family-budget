from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from fastapi_pagination.bases import AbstractPage
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.dependencies import get_current_active_user

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/", response_model=Page[schemas.User])
def get_users(db: Session = Depends(get_db), username: Union[str, None] = None) -> AbstractPage[schemas.User]:
    if username:
        return paginate(crud.get_filtered_users_by_username(db, username))
    return paginate(crud.get_all_users(db))


@users_router.get("/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> schemas.User:
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=400, detail=f"User with ID {user_id} doesn't exist")
    return crud.get_user_by_id(db, user_id)


@users_router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.User:
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user=user)


@users_router.get("/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)) -> schemas.User:
    return current_user
