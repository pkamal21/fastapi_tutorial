from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


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
    email: EmailStr
    password: str

# ----------------------------------------

class PostBase(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserOut

class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int

class PostVote(BaseModel):
    Post: Post
    votes: int

# ----------------------------------------

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None

# ----------------------------------------

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    class Config:
        orm_mode = True

