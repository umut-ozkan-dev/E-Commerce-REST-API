from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from products import product_page
from login import login_page
from home import home_page
from contact import contact_page
from shopping_cart import cart_page

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return home_page


@app.get("/products", response_class=HTMLResponse)
def products():
    return product_page


@app.get("/cart", response_class=HTMLResponse)
def cart():
    return cart_page


@app.get("/login", response_class=HTMLResponse)
def login():
    return login_page


@app.get("/contact", response_class=HTMLResponse)
def contact():
    return contact_page
