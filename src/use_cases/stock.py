from sqlalchemy.orm import Session
from domain.entities import Product

def check_stock(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        return product.quantity
    return None