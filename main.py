from products import product_page
from product_list import product_list
from login import login_page
from home import home_page
from contact import contact_page
from item import raw_item_page
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    return home_page


@app.get("/products", response_class=HTMLResponse)
def products():
    return product_page


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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found. Please enter values between 0-40",
    )


item_list = []


@app.post("/products/{id}", response_class=HTMLResponse)
def add_items_to_cart(id: int):
    item_list.append(id)
    return get_products(id)


@app.get("/cart", response_class=HTMLResponse)
def cart():
    with open("./pages/cart.html", "r", encoding="utf-8") as file:
        raw_html = file.read()

    result: str = ""
    total_price: float = 0

    if len(item_list) > 0:
        for id in item_list:
            with open("./templates/cart_item.html", "r", encoding="utf-8") as file:
                cart_item_html = file.read()

            cart_item_html = cart_item_html.replace(
                "{{Image}}", product_list[id]["Img"]
            )

            cart_item_html = cart_item_html.replace(
                "{{Name}}", product_list[id]["Name"]
            )

            cart_item_html = cart_item_html.replace(
                "{{Price}}", str(product_list[id]["Price"])
            )
            cart_item_html = cart_item_html.replace(
                "{{id}}", str(product_list[id]["id"])
            )

            cart_item_html = cart_item_html.replace("\n", "")
            cart_item_html = cart_item_html.replace("[", "")

            total_price += product_list[id]["Price"]
            result = result + cart_item_html

        for item in result:
            raw_html = raw_html.replace("{{cart_list}}", result)
            raw_html = raw_html.replace("{{TotalPrice}}", str(round(total_price, 2)))
            cart_page = raw_html
            return cart_page

    else:
        raw_html = raw_html.replace("{{cart_list}}", "Your Cart is Empty")
        raw_html = raw_html.replace("{{TotalPrice}}", "0")
        empty_cart_page = raw_html
        return empty_cart_page


@app.post("/cart/{id}", response_class=HTMLResponse)
def remove_item(id: int):
    item_list.remove(id)
    return cart()


@app.get("/styles.css")
def styles():
    return FileResponse("pages/styles.css")
