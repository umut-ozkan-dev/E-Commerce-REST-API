from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict
from product_list import product_list


class ProductBase(BaseModel):
    id: int = Field(ge=0)  # greater or equal to 0
    Name: str = Field(max_length=150)
    Price: float = Field(ge=0)
    Quantity: int = Field(ge=0)
    Category: str = Field(max_length=50)
    Img: str = Field(max_length=450)


PRODUCT_LIST : List[ProductBase] = ProductBase(*product_list)