# Real Projects often have a utils.py for biring tasks that are used everywhere, 
# like formatting dates or currency.

def format_currency(amount):
    """Formats a number into a readable USD string."""
    return f"${amount:,.2f}"

def print_receipt_header():
    print("-----------------------------")
    print("      OFFICIAL RECEIPT       ")
    print("-----------------------------")