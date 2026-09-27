FILEPATH = "./pages/cart.html"
from product_list import product_list

with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()

ids_of_items_added = [2, 7, 3]
result = ""

for id in ids_of_items_added:
    with open("./templates/cart_item.html", "r", encoding="utf-8") as file:
        cart_item_html = file.read()
    cart_item_html = cart_item_html.replace("{{Image}}", product_list[id]["Img"])
    cart_item_html = cart_item_html.replace("{{Name}}", product_list[id]["Name"])
    cart_item_html = cart_item_html.replace("{{Price}}", str(product_list[id]["Price"]))
    cart_item_html = cart_item_html.replace("\n", "")
    cart_item_html = cart_item_html.replace("[", "")

    result = result + (cart_item_html)

for item in cart_item_html:
    raw_html = raw_html.replace("{{cart_list}}", result)


cart_page = raw_html
