def create_order(order_id, amount):
    return {
        "order_id": order_id,
        "amount": amount,
        "status": "CREATED"
    }
