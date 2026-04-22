from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    nama_produk: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    category_id: int

class ProductUpdate(BaseModel):
    nama_produk: str
    harga: float
    stock: int