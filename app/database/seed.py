from faker import Faker
from app.database.db import SessionLocal, init_db
import random
from app.database.models import (
    Customer,
    Transaction
)
fake = Faker()

init_db()

db = SessionLocal()

for _ in range(100):

    customer = Customer(
        name=fake.name(),
        age=random.randint(24, 55),
        salary=random.randint(40000, 250000),
        credit_score=random.randint(650, 850),
        account_balance=random.randint(50000, 800000),
        employment_type=random.choice([
            "Salaried",
            "Business",
            "Self-Employed"
        ]),

        city=random.choice([
            "Mumbai",
            "Delhi",
            "Bangalore",
            "Hyderabad"
        ]),

        relationship_years=random.randint(1, 12),

        monthly_avg_transactions=random.randint(
            20,
            150
        ),

        last_loan_status=random.choice([
            "Closed Successfully",
            "Active",
            "Never Taken"
        ])
    )

    db.add(customer)

merchant_categories = [
    "Salary Credit",
    "Travel",
    "Shopping",
    "EMI Payment",
    "Dining",
    "Insurance",
    "Investment"
]

transaction_types = [
    "Credit",
    "Debit"
]


customers = db.query(Customer).all()

for customer in customers:

    for _ in range(
        random.randint(15, 40)
    ):

        transaction = Transaction(

            customer_id=customer.customer_id,

            transaction_type=random.choice(
                transaction_types
            ),

            amount=random.randint(
                1000,
                150000
            ),

            merchant_category=random.choice(
                merchant_categories
            ),

            transaction_month=random.choice([
                "January",
                "February",
                "March",
                "April"
            ])
        )

        db.add(transaction)

db.commit()

print("Seed data added")