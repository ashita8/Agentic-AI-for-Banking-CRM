from app.database.db import SessionLocal
from app.database.models import Customer

def get_high_value_customers(
    minimum_salary: int,
    minimum_credit_score: int
):

    db = SessionLocal()

    return db.query(Customer).filter(
        Customer.salary >= minimum_salary,
        Customer.credit_score >= minimum_credit_score
    ).all()