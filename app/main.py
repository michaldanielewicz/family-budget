from fastapi import FastAPI

from app import models
from app.database import engine
from app.endpoints.users import users_router


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(users_router)
