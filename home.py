FILEPATH = "./pages/home.html"

from products import product_list
from products import empty_list, product

with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()
    empty_list = ""

    home_page_items_list = [19, 15, 7, 21, 27, 40, 18, 22, 25, 23]
    for i in home_page_items_list:
        with open("./templates/product.html", "r", encoding="utf-8") as product_html:
            product = product_html.read()
            product = product.replace("{{Image}}", product_list[i]["Img"])
            product = product.replace("{{Id}}", str(product_list[i]["id"]))
            product = product.replace("{{Name}}", product_list[i]["Name"])
            product = product.replace("{{Price}}", str(product_list[i]["Price"]))
            empty_list += product

    home_page = raw_html.replace("{{empty_list}}", empty_list)
