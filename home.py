FILEPATH = "./pages/home.html"

from schemas import PRODUCT_LIST

from products import empty_list, product

with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()
    empty_list = ""

    home_page_items_list = [19, 15, 7, 21, 27, 40, 18, 22, 25, 23]
    for i in home_page_items_list:
        with open("./templates/product.html", "r", encoding="utf-8") as product_html:
            product = product_html.read()
            product = product.replace("{{Image}}", PRODUCT_LIST[i].Img)
            product = product.replace("{{Id}}", str(PRODUCT_LIST[i].id))
            product = product.replace("{{Name}}", PRODUCT_LIST[i].Name)
            product = product.replace("{{Price}}", str(PRODUCT_LIST[i].Price))
            empty_list += product

    home_page = raw_html.replace("{{empty_list}}", empty_list)
