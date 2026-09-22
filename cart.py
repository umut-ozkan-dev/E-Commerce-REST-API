FILEPATH = "./pages/cart.html"


with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()
    cart_page = raw_html
