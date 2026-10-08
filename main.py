from products import product_page
from product_list import product_list
from login import login_page
from home import home_page
from contact import contact_page
from schemas import PRODUCT_LIST
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


@app.get("/products/category/{category}", response_class=HTMLResponse)
def products_category(category: str):
    with open("./pages/products.html", "r", encoding="utf-8") as file:
        raw_html = f"{file.read()}"
    empty_list = ""
    for i in range(len(PRODUCT_LIST)):
        with open("./templates/product.html", "r", encoding="utf-8") as product_html:
            product = product_html.read()
            if PRODUCT_LIST[i].Category == category:
                product = product.replace("{{Image}}", PRODUCT_LIST[i].Img)
                product = product.replace("{{Id}}", str(PRODUCT_LIST[i].id))
                product = product.replace("{{Name}}", PRODUCT_LIST[i].Name)
                product = product.replace("{{Price}}", str(PRODUCT_LIST[i].Price))
                empty_list += product
                

    product_page = raw_html.replace("{{empty_list}}", empty_list)
    return product_page


@app.get("/login", response_class=HTMLResponse)
def login():
    return login_page


@app.get("/contact", response_class=HTMLResponse)
def contact():
    return contact_page


@app.get("/products/{id}", response_class=HTMLResponse)
def get_products(id: int):
    for product in PRODUCT_LIST:
        if product.id == id:
            with open("./pages/item.html", "r", encoding="utf-8") as file:
                raw = file.read()
                raw = raw.replace("{{id}}", str(PRODUCT_LIST[id].id))
                raw = raw.replace("{{Name}}", str(PRODUCT_LIST[id].Name))
                raw = raw.replace("{{Price}}", str(PRODUCT_LIST[id].Price))
                raw = raw.replace("{{Img}}", str(PRODUCT_LIST[id].Img))
                raw = raw.replace("{{Category}}", str(PRODUCT_LIST[id].Category))
                raw = raw.replace("{{Quantity}}", str(PRODUCT_LIST[id].Quantity))
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
    return cart()


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

            cart_item_html = cart_item_html.replace("{{Image}}", PRODUCT_LIST[id].Img)

            cart_item_html = cart_item_html.replace("{{Name}}", PRODUCT_LIST[id].Name)

            cart_item_html = cart_item_html.replace(
                "{{Price}}", str(PRODUCT_LIST[id].Price)
            )
            cart_item_html = cart_item_html.replace("{{id}}", str(PRODUCT_LIST[id].id))

            cart_item_html = cart_item_html.replace("\n", "")
            cart_item_html = cart_item_html.replace("[", "")

            total_price += PRODUCT_LIST[id].Price
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
