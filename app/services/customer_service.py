from app.database.db import SessionLocal
from app.database.models import Customer

def get_high_value_customers():

    db = SessionLocal()

    return db.query(Customer).filter(
        Customer.salary > 100000,
        Customer.credit_score > 720
    ).all()