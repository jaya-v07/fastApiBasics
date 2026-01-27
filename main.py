from fastapi import FastAPI
from model import Product
from database import SessionLocal
app = FastAPI()


products = [
Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", quantity=10),
Product(id=2, name="Smartphone", price=499.99, description="A latest model smartphone", quantity=25),
Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", quantity=15),
Product(id=4, name="Monitor", price=299.99, description="4K UHD Monitor", quantity=8),
Product(id=5, name="Keyboard", price=89.99, description="Mechanical keyboard", quantity=30),
Product(id=6, name="Mouse", price=49.99, description="Wireless mouse", quantity=20),
Product(id=7, name="Printer", price=149.99, description="All-in-one printer", quantity=12),
Product(id=8, name="Tablet", price=399.99, description="10-inch tablet", quantity=18),
Product(id=9, name="Webcam", price=79.99, description="HD webcam", quantity=22),
Product(id=10, name="Speakers", price=129.99, description="Bluetooth speakers", quantity=14)
]


@app.get("/")
def main_greeting():
    return "This is the main greeting page."
    
@app.get("/products")
def get_products():
    db = SessionLocal()
    db.query(Product)
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.delete("/products")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(index)
            return deleted_product
    return {"error": "Product not found"}

@app.put("/products")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    return {"error": "Product not found"}