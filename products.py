from typing import Dict
from product_list import product_list

FILEPATH = "./pages/products.html"


with open(FILEPATH) as f:
    product_page = f"{f.read()}"


for i in range(len(product_list)):
    product_page += f""" 
        
                    
                    <div class ="inside_items"> 
                    <img src="{product_list[i]["Img"]}" width=130>
                                        <hr>
                    <strong ><a href="./products/{product_list[i]["id"]}">{product_list[i]["Name"]}</a></strong>
                    <br><br>
                                        <br><div class="price">
                    ${product_list[i]["Price"]}</div> 
                    </div>  
                    """
