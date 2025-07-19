from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from ...database.database import get_db
from ...models.transaction import Transaction
from ...schemas.transaction import TransactionCreate, TransactionSchema

router = APIRouter()


@router.post("/", response_model=TransactionSchema)
def create_transaction(item: TransactionCreate, db: Session = Depends(get_db)):
    # db_transaction = Transaction(**item.model_dump(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    # db.add(db_transaction)
    # db.commit()
    # db.refresh(db_transaction)
    # return db_transaction
    pass

@router.get("/", response_model=list[TransactionSchema])
def list_transactions(db: Session = Depends(get_db)):
    # return db.query(Transaction).all()
    pass


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