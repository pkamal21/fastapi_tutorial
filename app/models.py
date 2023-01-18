from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        server_default=text('now()'), nullable=False)
    phone_number = Column(String)
    # team = relationship('Team', backref="user")

class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    stock1 = Column(Integer, nullable=True)
    stock2 = Column(Integer, nullable=True)
    stock3 = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                    server_default=text('now()'), nullable=False)
    modified_at = Column(TIMESTAMP(timezone=True),
                    server_default=text('now()'), nullable=False)

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, nullable=False)
    stock_name = Column(String, nullable=False)
    stock_price = Column(Float, nullable=False)
    stock_external_id = Column(String, nullable=True)
    sector = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), 
                    server_default=text('now()'), nullable=False)
    modified_at = Column(TIMESTAMP(timezone=True),
                    server_default=text('now()'), nullable=False)
