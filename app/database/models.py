from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Float)
    credit_score = Column(Integer)
    account_balance = Column(Float)