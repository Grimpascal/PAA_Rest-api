from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.transaction import Transaction
from models.transaction_detail import TransactionDetail
from models.product import Product
from schemas.transaction import TransactionCreate
from dependencies import get_current_user
from models.user import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(payload: TransactionCreate, db: Session = Depends(get_db),user: User = Depends(get_current_user)):

    total_price = 0

    # buat transaksi dulu
    new_transaction = Transaction(user_id=payload.user_id, total_price=0, status="pending")
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    for item in payload.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")

        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Stock not enough for product {product.nama_produk}")

        subtotal = product.harga * item.quantity
        total_price += subtotal

        product.stock -= item.quantity

        detail = TransactionDetail(
            transaction_id=new_transaction.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.harga
        )

        db.add(detail)

    new_transaction.total_price = total_price

    db.commit()

    return {"status": "success", "data": new_transaction}