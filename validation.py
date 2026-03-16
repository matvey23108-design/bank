def validate_positive_float(value):
    try:
        value = float(value)
        return value > 0
    except ValueError:
        return False

