from typing import Dict
from product_list import product_list

FILEPATH = "./pages/products.html"


with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = f"{file.read()}"
    empty_list = ""
    for i in range(len(product_list)):
        with open("./templates/product.html", "r", encoding="utf-8") as product_html:
            product = product_html.read()
            product = product.replace("{{Image}}", product_list[i]["Img"])
            product = product.replace("{{Id}}", str(product_list[i]["id"]))
            product = product.replace("{{Name}}", product_list[i]["Name"])
            product = product.replace("{{Price}}", str(product_list[i]["Price"]))
            empty_list += product

    product_page = raw_html.replace("{{empty_list}}", empty_list)
