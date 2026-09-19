FILEPATH = "./pages/home.html"

from products import product_list

with open(FILEPATH) as f:
    home_page = f.read()


for i in range(8):
    home_page += f""" 
                    <br>
                    <div class = "items"> 
                    <div class ="inside_items"> 
                    <img src="{product_list[i]["Img"]}" width=130>
                                        <hr>
                    <strong>{product_list[i]["Name"]}</strong>
                    <br>
                                        <br>
                    ${product_list[i]["Price"]} <br> 
                    </div>
                    </div>
                    <br><br><br>

                    """
