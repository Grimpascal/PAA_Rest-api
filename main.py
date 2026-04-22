from fastapi import FastAPI
from database import engine, Base
from sqlalchemy import text
from models import user, category, product, transaction, transaction_detail
from routes import product
from routes import transaction
from routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product.router)
app.include_router(transaction.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "API jalan"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"result": "Database connected"}