from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.schemas import ProductCreate, ProductOut
from use_cases.product import create_product, list_product
from use_cases.stock import check_stock
from core.database import get_connection
from core.config import settings

router = APIRouter()

@router.post('/', response_model=ProductOut)
def add_product(product: ProductCreate, db: Session = Depends(get_connection)):
    return create_product(db, product)

@router.get('/', response_model=list[ProductOut])
def get_all_products(db: Session = Depends(get_connection)):
    return list_product(db)

@router.get('/{product_id}/stock', tags=['Estoques'])
def get_stock(product_id: int, db: Session = Depends(get_connection)):
    stock = check_stock(db, product_id)
    if stock is None:
        raise HTTPException(
            status_code=404,
            detail=settings.message_product_not_found
        )
    return {
        'product_id': product_id,
        'stock': stock
    }
