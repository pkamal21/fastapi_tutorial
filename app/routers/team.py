from fastapi import Depends, HTTPException, status, APIRouter
from app import models, oauth2, schemas, utils
from sqlalchemy.orm import Session
from app.database import get_db
from sqlalchemy import func

router = APIRouter(prefix="/team", tags=["Team"])

def get_stock_data(id: int, db: Session = Depends(get_db)):
    id = int(id)
    return db.query(models.Stock).filter(models.Stock.id == id).first()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_team(team: schemas.Team, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    
    team = models.Team(user_id=current_user.id, **team.dict())
    
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

@router.put("/{id}")
def update_team(team: schemas.Team, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    ...

@router.get("/")
def get_latest_team(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    team = db.query(models.Team).filter(models.Team.user_id == current_user.id).order_by(models.Team.created_at).first()
    team_details = [get_stock_data(team.stock1, db), get_stock_data(team.stock2, db), get_stock_data(team.stock3, db)]
    return team_details

@router.get("/{id}")
def get_team(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    team = db.query(models.Team).filter(models.Team.id == id, models.Team.user_id == current_user.id).first()
    team_details = [get_stock_data(team.stock1, db), get_stock_data(team.stock2, db), get_stock_data(team.stock3, db)]
    return team_details

@router.get("/all")
def get_teams(db: Session = Depends(get_db),  
              current_user: models.User = Depends(oauth2.get_current_user), 
              limit: int = 10, skip: int = 0):
    """
    Returns teams created by the current user
    """

    teams = db.query(models.Team).filter(models.Team.user_id == current_user.id).offset(skip).limit(limit).all()
    stocks = []
    for team in teams:
        team_details = [get_stock_data(team.stock1, db), get_stock_data(team.stock2, db), get_stock_data(team.stock3, db)]
        
        stocks.append(team_details)
    return stocks
