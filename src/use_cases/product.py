from sqlalchemy.orm import Session
from domain.entities import Product
from domain.schemas import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def list_product(db: Session):
    return db.query(Product).all()
