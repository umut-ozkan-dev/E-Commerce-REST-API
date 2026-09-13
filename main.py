from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from products import product_list, final_string
from home import homepage

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return homepage


@app.get("/products", response_class=HTMLResponse)
def products():
    return final_string


@app.get("/contact")
def contact():
    return {"message": {"email": "ecommerce@gmail.com", "location": "Ankara, Turkey"}}


@app.get("/cart")
def cart():
    return {"message": {"email": "Your cart is empty"}}
