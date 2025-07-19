from fastapi import FastAPI
from .routers import transaction

app = FastAPI()
app.include_router(transaction.router, prefix="/transactions", tags=["transactions"])

# from ..database.database import engine, Base

# Base.metadata.create_all(bind=engine)