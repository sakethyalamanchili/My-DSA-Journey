# We will simulate a database using a Python dictionary. 
# This file is responsible only for finding data.

# A mock database of products
_product_db = {
    101 : {"name": "Wireless Headphones", "price": 99.99},
    102 : {"name": "Mechanical Keyboard", "price": 145.50},
    103 : {"name": "Gaming Mouse", "price": 59.99}
}

def get_product_by_id(product_id):
    """Simulates fetching a row from a database."""
    result = _product_db.get(product_id)
    
    if result:
        return result
    else:
        raise ValueError(f"ProductID {product_id} not found.")