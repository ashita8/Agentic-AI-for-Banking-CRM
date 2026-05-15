from app.database.db import SessionLocal
from app.database.models import Customer

def fetch_high_value_customers():

    db = SessionLocal()

    customers = db.query(Customer).filter(
        Customer.salary > 100000,
        Customer.credit_score > 720
    ).all()

    return customers