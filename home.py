FILEPATH = "./pages/home.html"

from products import product_list

with open(FILEPATH) as f:
    home_page = f.read()


for i in range(12):
    home_page += f""" 
        
                    
                    <div class ="inside_items"> 
                    <img src="{product_list[i]["Img"]}" width=130>
                                        <hr>
                    <strong ><a href="./products/{product_list[i]["id"]}">{product_list[i]["Name"]}</a></strong>
                    <br><br>
                                        <br><div class="price">
                    ${product_list[i]["Price"]}</div> 
                    </div>  
                    """
