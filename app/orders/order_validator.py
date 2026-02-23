def validate_order(order):
    if not order.get("order_id"):
        raise ValueError("Missing order ID")
    return True
