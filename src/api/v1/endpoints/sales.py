from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.schemas import SaleCreate
from use_cases.sale import create_sale
from core.database import get_connection
from core.config import settings

router = APIRouter()

@router.post('/',name='Nova venda', description='Realiza o cadastro de uma nova venda')
def sell_product(sale: SaleCreate, db: Session = Depends(get_connection)):
    new_sale = create_sale(db, sale)
    if not new_sale:
        raise HTTPException(
            status_code=400,
            detail=settings.message_insufficient_stock
        )
    return new_sale