from pydantic import BaseModel


class BudgetBase(BaseModel):
    title: str
    description: str | None = None


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    budgets: list[Budget] = []

    class Config:
        orm_mode = True
