from fastapi import FastAPI

STUDENT_N = 5

app = FastAPI(title=f"Order Service N{STUDENT_N}")

ORDERS = []

@app.post("/orders")
def create_order(order: dict):
    new_order = {
        "id": len(ORDERS) + 1,
        "student_id": STUDENT_N,
        "product_id": order["product_id"],
        "quantity": order["quantity"]
    }

    ORDERS.append(new_order)

    return new_order


@app.get("/orders")
def get_orders():
    return {
        "student_id": STUDENT_N,
        "orders": ORDERS
    }