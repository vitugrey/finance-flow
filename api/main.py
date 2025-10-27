from fastapi import FastAPI
from api.database.database import Base, engine
from api.routers import transaction

# Criar tabelas no DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinanceFlow API")

# Incluir rotas
app.include_router(transaction.router)