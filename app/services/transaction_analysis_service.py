def analyze_transactions(
    customers,
    transactions
):

    customer_transaction_map = {}

    for txn in transactions:

        customer_id = txn[
            "customer_id"
        ]

        if customer_id not in (
            customer_transaction_map
        ):
            customer_transaction_map[
                customer_id
            ] = []

        customer_transaction_map[
            customer_id
        ].append(txn)

    enriched_customers = []

    for customer in customers:

        txns = customer_transaction_map.get(
            customer["customer_id"],
            []
        )

        salary_credits = len([
            txn for txn in txns
            if txn[
                "merchant_category"
            ] == "Salary Credit"
        ])

        emi_payments = len([
            txn for txn in txns
            if txn[
                "merchant_category"
            ] == "EMI Payment"
        ])

        investments = len([
            txn for txn in txns
            if txn[
                "merchant_category"
            ] == "Investment"
        ])

        total_spend = sum([
            txn["amount"]
            for txn in txns
            if txn[
                "transaction_type"
            ] == "Debit"
        ])

        customer[
            "transaction_insights"
        ] = {
            "salary_credit_frequency":
                salary_credits,

            "emi_payment_count":
                emi_payments,

            "investment_activity":
                investments,

            "total_debit_spend":
                total_spend
        }

        enriched_customers.append(
            customer
        )

    return enriched_customers