from typing import Dict
from product_list import product_list

FILEPATH = "./pages/products.html"


with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = f"{file.read()}"
    empty_list = ""
    for i in range(len(product_list)):
        product = f"""  <div class ="inside_items"> 
                        <img src="{product_list[i]["Img"]}" width=130>
                        <hr>
                        <strong ><a href="./products/{product_list[i]["id"]}">{product_list[i]["Name"]}</a></strong>
                        <br><br><br><div class="price">
                        ${product_list[i]["Price"]}</div> 
                        </div>  
                        """
        empty_list += product
        
    product_page = raw_html.replace("{{empty_list}}", empty_list)
