from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from products import product_list

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Tal E-Commerce"}


@app.get("/products")
def products():
    return product_list


@app.get("/contact")
def contact():
    return {"message": {"email": "ecommerce@gmail.com", "location": "Ankara, Turkey"}}
