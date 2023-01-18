from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import List, Optional


# -----------------------------USER--------------------------

class UserBase(BaseModel):
    email: EmailStr
    class Config:
        orm_mode = True

class UserOut(UserBase):
    created_at: datetime
    id: int

class UserInput(UserBase):
    password: str


class UserLogin(BaseModel):
    username: EmailStr
    password: str

# ------------------------------------STOCK---------------------------------

class Stock(BaseModel):
    stock_name: str
    stock_external_id: str
    stock_price: float

    class Config:
        orm_mode = True

# -----------------------------------TEAM-------------------------------------

class Team(BaseModel):
    stock1: str
    stock2: str
    stock3: str

    class Config:
        orm_mode = True

# ---------------------------------TOKEN---------------------------------

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None
