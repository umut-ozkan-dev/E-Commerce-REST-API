from typing import Dict

product_list: list[Dict] = [
    {"id": 1, "Name": "Alarm Clock", "Price": 9.90, "In Stock": True},
    {"id": 2, "Name": "Wire Headphone", "Price": 29.90, "In Stock": True},
    {"id": 3, "Name": "Mouse", "Price": 7.90, "In Stock": True},
    {"id": 4, "Name": "HDW Monitor", "Price": 69.90, "In Stock": True},
    {"id": 5, "Name": "E2 Bud Headphone", "Price": 29.90, "In Stock": True},
    {"id": 6, "Name": "Leadwise Monitor", "Price": 79.90, "In Stock": True},
]

FILEPATH = "./pages/products.html"


with open(FILEPATH) as f:
    product_page = f"{f.read()}"


for i in range(len(product_list)):
    product_page += f""" 
                    <div class = "items"> 
                    <div class ="inside_items"> 
                    Name : {product_list[i]["Name"]} <br>
                    Price : {product_list[i]["Price"]}$<br> 
                    In Stock : {product_list[i]["In Stock"]}<br> 
                    <button> Add to Cart</button> 
                    </div>
                    </div>
                    <br><br><br>

                    """
