from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.transaction import Transaction
from api.schemas.transaction import TransactionCreate, TransactionSchema

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionSchema)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.model_dump(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@router.get("/", response_model=list[TransactionSchema])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


@router.put("/{transaction_id}", response_model=TransactionSchema)
def update_transaction(transaction_id: int, item: TransactionCreate, db: Session = Depends(get_db)):
    # db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    # if not db_transaction:
    #     raise HTTPException(404, "Transação não encontrada.")
    # for key, value in item.model_dump().items():
    #     setattr(db_transaction, key, value)
    # db.commit()
    # db.refresh(db_transaction)
    # return db_transaction
    pass


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    # db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    # if not db_transaction:
    #     raise HTTPException(404, "Transação não encontrada.")
    # db.delete(db_transaction)
    # db.commit()
    # return {
    #     "detail": "transaction deleted successfully",
    #     "transaction": db_transaction.description
    # }
    pass
