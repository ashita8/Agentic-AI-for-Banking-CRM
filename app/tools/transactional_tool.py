from app.database.db import (
    SessionLocal
)

from app.database.models import (
    Transaction
)


def fetch_customer_transactions(
    customer_ids
):

    db = SessionLocal()

    transactions = db.query(
        Transaction
    ).filter(
        Transaction.customer_id.in_(
            customer_ids
        )
    ).all()

    serialized = []

    for txn in transactions:

        serialized.append({
            "customer_id":
                txn.customer_id,

            "transaction_type":
                txn.transaction_type,

            "amount":
                txn.amount,

            "merchant_category":
                txn.merchant_category,

            "transaction_month":
                txn.transaction_month
        })

    return serialized