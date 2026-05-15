from faker import Faker
from app.database.db import SessionLocal, init_db
from app.database.models import Customer
import random

fake = Faker()

init_db()

db = SessionLocal()

for _ in range(100):

    customer = Customer(
        name=fake.name(),
        age=random.randint(24, 55),
        salary=random.randint(40000, 250000),
        credit_score=random.randint(650, 850),
        account_balance=random.randint(50000, 800000)
    )

    db.add(customer)

db.commit()

print("Seed data added")