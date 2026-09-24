from products import product_page, product_list
from login import login_page
from home import home_page
from contact import contact_page
from cart import cart_page
from item import raw_item_page
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from mako.lookup import TemplateLookup

# Configure the template directory
templates = TemplateLookup(directories=["templates"], input_encoding="utf-8")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


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


@app.get("/products/{id}", response_class=HTMLResponse)
def get_products(id: int):
    with open("./pages/item.html", "r", encoding="utf-8") as file:
        raw_item_page = file.read()

    raw_item_page = raw_item_page.replace("{{id}}", str(product_list[id]["id"]))
    raw_item_page = raw_item_page.replace("{{Name}}", str(product_list[id]["Name"]))
    raw_item_page = raw_item_page.replace("{{Price}}", str(product_list[id]["Price"]))
    raw_item_page = raw_item_page.replace("{{Img}}", str(product_list[id]["Img"]))
    raw_item_page = raw_item_page.replace("{{Category}}", str(product_list[id]["Category"]))
    raw_item_page = raw_item_page.replace("{{Quantity}}", str(product_list[id]["Quantity"]))
    item_page = raw_item_page
    return item_page


@app.get("/styles.css")
def styles():
    return FileResponse("pages/styles.css")
