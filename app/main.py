from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app import models
from app.database import engine
from app.endpoints.auth import auth_router
from app.endpoints.users import users_router

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
add_pagination(app)
app.include_router(users_router)
app.include_router(auth_router)
