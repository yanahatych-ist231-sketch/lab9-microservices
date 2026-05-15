from fastapi import FastAPI, HTTPException

STUDENT_N = 5

app = FastAPI(title="Product Service")

PRODUCTS = {
    501: {
        "id": 501,
        "name": "Laptop Dell",
        "price": 1200.0,
        "stock": 5
    },
    502: {
        "id": 502,
        "name": "Mouse Logitech",
        "price": 25.0,
        "stock": 50
    }
}

@app.get("/products")
def get_products():
    return {
        "student_id": STUDENT_N,
        "products": list(PRODUCTS.values())
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "student_id": STUDENT_N,
        "product": PRODUCTS[product_id]
    }