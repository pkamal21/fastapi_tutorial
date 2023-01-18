from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import HTMLResponse

from app import models, oauth2, schemas
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/stock", tags=["stock"])

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_team(stock: schemas.Stock, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    """
    Creates a stock
    """
    new_stock = models.Stock(**stock.dict())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)

    return new_stock


@router.get("/{pref}")
def read_item(pref: str, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    stocks = db.query(models.Stock).filter(models.Stock.stock_name.startswith(pref)).all()
    return stocks
