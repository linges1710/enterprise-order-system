def process_payment(order_id, amount):
    if amount <= 0:
        raise ValueError("Invalid amount")
    return True
