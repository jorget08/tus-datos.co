from fastapi import APIRouter, Depends
from config.db import conn
from models.product import products
from schemas.product import Product, UpdateProduct
from auth.auth import AuthHandler


product = APIRouter()
auth_handler = AuthHandler()


@product.get('/products')
def list_products(email=Depends(auth_handler.auth_wrapper)):
    return conn.execute(products.select()).fetchall()

@product.post('/products')
def create_product(product:Product, email=Depends(auth_handler.auth_wrapper)):
    new_product = {"name": product.name, "description": product.description, "price": product.price}
    result = conn.execute(products.insert().values(new_product))
    return conn.execute(products.select().where(products.c.id == result.lastrowid)).first()

@product.get('/products/{id}')
def list_a_product(id:str, email=Depends(auth_handler.auth_wrapper)):
    return conn.execute(products.select().where(products.c.id == id)).first()

@product.put('/products/{id}')
def update_product(product:UpdateProduct, id: str, email=Depends(auth_handler.auth_wrapper)):
    if product.name:
        conn.execute(products.update().values(name=product.name).where(products.c.id == id))
    if product.description:
        conn.execute(products.update().values(description=product.description).where(products.c.id == id))
    if product.price:
        conn.execute(products.update().values(price=product.price).where(products.c.id == id))
    return "Product updated successfully"

@product.delete('/products/{id}')
def delete_product(id: str, email=Depends(auth_handler.auth_wrapper)):
    conn.execute(products.delete().where(products.c.id == id))
    return "Deleted"