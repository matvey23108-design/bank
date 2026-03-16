
from validation import validate_positive_float

def calculate_credit(amount, interest_rate, term_years):
   
    amount = validate_positive_float(amount)
    interest_rate = validate_positive_float(interest_rate)
    term_years = validate_positive_float(term_years)

   
    monthly_payment = (amount * interest_rate / 12) + (amount / (term_years * 12))
    return round(monthly_payment, 2)
