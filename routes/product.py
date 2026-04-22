from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate
from dependencies import admin_only
from models.user import User

router = APIRouter()

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return {"status": "success", "data": products}

@router.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"status": "success", "data": product}

@router.post("/products")
def create_product(payload: ProductCreate, db: Session = Depends(get_db), user: User = Depends(admin_only)):
    new_product = Product(
        nama_produk=payload.nama_produk,
        harga=payload.price,
        stock=payload.stock,
        category_id=payload.category_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {"status": "success", "data": new_product}

@router.put("/products/{id}")
def update_product(id: int, payload: ProductUpdate, db: Session = Depends(get_db), user: User = Depends(admin_only)):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.nama_produk = payload.nama_produk
    product.harga = payload.price
    product.stock = payload.stock

    db.commit()
    db.refresh(product)

    return {"status": "success", "data": product}

@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db), user: User = Depends(admin_only)):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"status": "success", "message": "Product deleted"}