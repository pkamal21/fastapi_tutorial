from typing import List, Optional
from app import models, schemas, oauth2, utils

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/posts", tags=['posts'])


@router.get("/", response_model=List[schemas.PostVote])
def get_posts(db: Session = Depends(get_db),  
              current_user: models.User = Depends(oauth2.get_current_user), 
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    """
    Returns posts created by the current user
    """
    # posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).\
    #            filter(models.Post.title.contains(search)).offset(skip).\
    #            limit(limit).all()
    
    p = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).\
           join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).\
           group_by(models.Post.id).filter(models.Post.title.contains(search)).offset(skip).\
               limit(limit).all()
    return p

@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    """
    Creates a post for the current user id with the PostCreate schema
    """
    new_post = models.Post(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}", response_model=schemas.PostVote)
def get_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    """
    Get post for a particular id
    """
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).\
           join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).\
           group_by(models.Post.id).filter(models.Post.id == id).first()

    utils.verify_current_user(current_user, post.user_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    utils.verify_current_user(current_user, post_query.first().user_id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="post with id not found")
    post_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "succesfully deleted post"}

@router.put("/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    utils.verify_current_user(current_user, post_query.first().user_id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} not found")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
