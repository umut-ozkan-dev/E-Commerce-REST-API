from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from products import product_list, final_string
from login import login_page
from home import homepage
from contact import contact_page

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return homepage


@app.get("/products", response_class=HTMLResponse)
def products():
    return final_string


@app.get("/contact", response_class=HTMLResponse)
def contact():
    return contact_page


@app.get("/cart")
def cart():
    return {"message": {"email": "Your cart is empty"}}


@app.get("/login", response_class=HTMLResponse)
def login():
    return login_page
