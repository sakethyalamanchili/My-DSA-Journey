def process_credit_card(amount):
    print(f"Connecting to Visa/Mastercard server...")
    print(f"Authorized charge of {amount}")
    return True

def process_paypal(amount):
    print(f"Redirecting to PayPal...")
    print(f"User approved transaction of {amount}")
    return True