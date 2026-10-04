from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict
from product_list import product_list


class ProductBase(BaseModel):
    id: int = Field(ge=0)  # greater or equal to 0
    Name: str = Field(max_length=150)  # maximum length is 150 characters
    Price: float = Field(ge=0)
    Quantity: int = Field(ge=0)
    Category: str = Field(max_length=50)
    Img: str = Field(max_length=450)


PRODUCT_LIST: List[ProductBase] = []
for i in range(len(product_list)):
    PRODUCT_LIST.append(
        ProductBase(
            id=product_list[i]["id"],
            Name=product_list[i]["Name"],
            Price=product_list[i]["Price"],
            Quantity=product_list[i]["Quantity"],
            Category=product_list[i]["Category"],
            Img=product_list[i]["Img"],
        )
    )



 