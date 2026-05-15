def recommend_loan_product(customer, score):

    if score >= 80:
        return "Pre-approved Premium Personal Loan"

    if score >= 60:
        return "Instant Personal Loan"

    return "Standard Personal Loan"