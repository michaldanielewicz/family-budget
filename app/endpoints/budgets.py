from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from fastapi_pagination.bases import AbstractPage
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.endpoints.auth import get_current_active_user

budgets_router = APIRouter()


@budgets_router.get("/budgets/", response_model=Page[schemas.Budget])
def get_budgets(
    db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)
) -> AbstractPage[schemas.Budget]:
    return paginate(crud.get_budgets_by_owner_id(db=db, owner_id=current_user.id))


@budgets_router.post("/budgets/", response_model=schemas.Budget)
def create_budget(
    budget: schemas.BudgetCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
):
    return crud.create_budget(db=db, budget=budget, owner_id=current_user.id)
