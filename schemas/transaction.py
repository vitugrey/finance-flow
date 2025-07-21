from pydantic import BaseModel
from datetime import datetime, date
from enum import Enum


class TransactionType(str, Enum):
    INCOME = "Income"
    EXPENSE = "Expense"


class TransactionBase(BaseModel):
    description: str 
    value: float
    category: str
    date: date
    is_credit: bool
    is_fixed_expense: bool
    transaction_type: TransactionType


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class TransactionSchema(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
