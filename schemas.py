from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    id: int = Field(max_digits=3)
    Name: str = Field(max_length=150)
    Price: float = Field(max_digits=6)
    Quantity: int = Field(max_digits=2)
    Category: str = Field(max_length=50)
    Img: str = Field(max_length=450)


class AddProduct(BaseModel):
    pass
