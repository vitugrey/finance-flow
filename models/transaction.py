from datetime import datetime
from sqlalchemy import (Column, Integer, String, Float, Text,
                        ForeignKey, Boolean, DateTime, Date, CHAR)
from sqlalchemy.orm import relationship
from ..database.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(Text)
    value = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    date = Column(Date, nullable=False)
    is_credit = Column(Boolean, nullable=False, default=False)
    is_fixed_expense = Column(Boolean, nullable=False, default=False)
    transaction_type = Column(CHAR(10), nullable=False, default="Expense")  # Income or Expense
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False)

    category = relationship("Category")