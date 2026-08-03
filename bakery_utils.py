# bakery_utils.py

BAKERY_NAME = "Ang Bakery ni Josh na pinaka Malupet"

def calculate_total(price, quantity, tax_rate=0.08):

    subtotal = price * quantity
    total = subtotal + (subtotal * tax_rate)
    return round(total, 2)

def print_receipt(item_name, total_price):
    
    print(f"\n--- {BAKERY_NAME} ---")
    print(f"Item: {item_name}")
    print(f"Total Due: ${total_price}")
    print("Thank you for your business!\n")