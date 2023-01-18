from typing import List
import app.models as models
import app.schemas as schemas
import app.utils as utils
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter(prefix="/user", tags=['users'])

@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserInput, db: Session = Depends(get_db)):

    user_found = db.query(models.User).filter(models.User.email == user.email).first()

    if user_found:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Enter correct email")
    
    hashed_pwd = utils.get_hash(user.password)
    print(user.dict())
    user.password = hashed_pwd
    user = models.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
