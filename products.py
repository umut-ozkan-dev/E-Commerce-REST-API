from typing import Dict
from schemas import PRODUCT_LIST

FILEPATH = "./pages/products.html"


with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = f"{file.read()}"
    empty_list = ""
    for i in range(len(PRODUCT_LIST)):
        with open("./templates/product.html", "r", encoding="utf-8") as product_html:
            product = product_html.read()
            product = product.replace("{{Image}}", PRODUCT_LIST[i].Img)
            product = product.replace("{{Id}}", str(PRODUCT_LIST[i].id))
            product = product.replace("{{Name}}", PRODUCT_LIST[i].Name)
            product = product.replace("{{Price}}", str(PRODUCT_LIST[i].Price))
            empty_list += product

    product_page = raw_html.replace("{{empty_list}}", empty_list)
