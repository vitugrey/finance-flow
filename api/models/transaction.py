from datetime import datetime
from sqlalchemy import (Column, Integer, String, Float, Text,
    Boolean, DateTime, DateTime)
from sqlalchemy.sql import func
from api.database.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(Text, nullable=True)
    value = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    transaction_type = Column(String, nullable=False, default="Expense")  # Income or Expense
    is_credit = Column(Boolean, nullable=False, default=False)
    is_fixed_expense = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
