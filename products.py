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
                    <strong>{product_list[i]["Name"]}</strong>
                    <br>
                                        <br>
                    ${product_list[i]["Price"]} <br> 
                    </div>  
                    """
