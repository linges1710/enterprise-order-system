def validate_order(order):
    if not order.get("order_id"):
        raise ValueError("Missing order ID")

    if not order.get("amount"):
        raise ValueError("Amount missing")

    if order.get("amount") <= 0:
        raise ValueError("Invalid order amount")

    if not order.get("customer_id"):
        raise ValueError("Customer ID missing")

    return True
