from products import product_page, product_list
from login import login_page
from home import home_page
from contact import contact_page
from cart import cart_page
from item import raw_item_page
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

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
    for product in product_list:
        if product.get("id") == id:
            with open("./pages/item.html", "r", encoding="utf-8") as file:
                raw = file.read()
                raw = raw.replace("{{id}}", str(product_list[id]["id"]))
                raw = raw.replace("{{Name}}", str(product_list[id]["Name"]))
                raw = raw.replace("{{Price}}", str(product_list[id]["Price"]))
                raw = raw.replace("{{Img}}", str(product_list[id]["Img"]))
                raw = raw.replace("{{Category}}", str(product_list[id]["Category"]))
                raw = raw.replace("{{Quantity}}", str(product_list[id]["Quantity"]))
                item_page = raw
            return item_page
    raise HTTPException(status_code=404)


@app.get("/styles.css")
def styles():
    return FileResponse("pages/styles.css")
