# Now watch how clean main.py is. It doesn't care how the database works 
# Or how the payment connects. It just imports and uses them.

# 1. Import local helper module
import utils

# 2. Import from the database package
from database import inventory

# 3. Import from payments (Clean import thanks to __init__.py!)
from payments import process_credit_card

def process_order(product_id):
    try:
        # Step A: Fetch Product
        print(f"Searching for product {product_id}...")
        product = inventory.get_product_by_id(product_id)
        
        name = product['name']
        price = product['price']
        
        # Step B: Display Receipt using Utils
        utils.print_receipt_header()
        print(f"Item: {name}")
        print(f"Price: {utils.format_currency(price)}")
        
        # Step C: Process Payment
        print("\n--- Starting Transaction ---")
        process_credit_card(price)
        
        print("\nSUCCESS: Order has been shipped!")
    
    except ValueError as e:
        print(f"ERROR: {e}")
        
if __name__ == "__main__":
    # Let's try to buy the keyboard (ID 102)
    process_order(103)