from sqlalchemy.orm import Session
from domain.entities import Product, Sale
from domain.schemas import SaleCreate

def create_sale(db: Session, sale: SaleCreate):
    product = db.query(Product).filter(Product.id == sale.product_id).first()

    if not product or  product.quantity < sale.quantity:
        return None
    
    product.quantity -= sale.quantity

    new_sale = Sale(
        quantity=sale.quantity,
        product_id=sale.product_id
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale

def get_sale(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()

def list_sale(db: Session):
    return db.query(Sale).all()
