from validation import validate_positive_float

def calculate_deposit(amount, interest_rate, term_years):
    amount = validate_positive_float(amount)
    interest_rate = validate_positive_float(interest_rate)
    term_years = validate_positive_float(term_years)

    total_amount = amount * (1 + interest_rate * term_years)
    return round(total_amount, 2)
