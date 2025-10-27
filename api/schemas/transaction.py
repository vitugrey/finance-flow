from pydantic import BaseModel
from datetime import datetime, date
from enum import Enum
from typing import Optional


class TransactionType(str, Enum):
    INCOME = "Income"
    EXPENSE = "Expense"


class TransactionBase(BaseModel):
    description: Optional[str]
    value: float
    category: str
    date: date
    transaction_type: TransactionType
    is_credit: bool
    is_fixed_expense: bool


class TransactionCreate(TransactionBase):
    pass


class TransactionSchema(TransactionBase):
    id: int
    created_at: datetime #possivel erro
    updated_at: datetime

    class Config:
        from_attributes = True
