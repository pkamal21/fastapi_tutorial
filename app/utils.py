from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_hash(pwd: str):
    return pwd_context.hash(pwd)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def verify_current_user(current_user, object_user_id):
    if current_user.id != object_user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="This activity is not authorized")
