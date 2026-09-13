from typing import Dict

product_list: list[Dict] = [
    {"id": 1, "Name": "Alarm Clock", "Price": 9.90, "In Stock": True},
    {"id": 2, "Name": "Wire Headphone", "Price": 29.90, "In Stock": True},
    {"id": 3, "Name": "Mouse", "Price": 7.90, "In Stock": True},
    {"id": 4, "Name": "HDW Monitor", "Price": 69.90, "In Stock": True},
    {"id": 5, "Name": "E2 Bud Headphone", "Price": 29.90, "In Stock": True},
    {"id": 6, "Name": "Leadwise Monitor", "Price": 79.90, "In Stock": True},
]


final_string = f"""
<h1>Welcome to Products</h1> 
<hr>
<br>
"""
for i in range(len(product_list)):
    final_string += f""" 
                    <p>Name : {product_list[i]["Name"]}</p>
                    <p>Price : {product_list[i]["Price"]} $</p> 
                    <p>In Stock : {product_list[i]["In Stock"]}</p> 
                    <br>
                    """
