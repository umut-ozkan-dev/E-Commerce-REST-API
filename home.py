FILEPATH = "./pages/home.html"

from products import product_list
from products import empty_list

with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()
    home_page = raw_html.replace("{{empty_list}}",empty_list)
   
    