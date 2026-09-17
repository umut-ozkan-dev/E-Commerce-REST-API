from products import product_page
from login import login_page
from home import home_page
from contact import contact_page
from cart import cart_page

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from mako.lookup import TemplateLookup

# Configure the template directory
templates = TemplateLookup(directories=["templates"], input_encoding="utf-8")

app = FastAPI()


@app.get("/home", response_class=HTMLResponse)
async def home2(request: Request):
    template = templates.get_template("index.html")

    html = template.render(
        title="My FastAPI App",
        message="Hello from FastAPI and Mako!",
        username="e",
        is_logged_in=True,
    )

    return HTMLResponse(content=html)


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


@app.get("/styles.css")
def styles():
    return FileResponse("pages/styles.css")
