from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_trade(db: Session, trade: schemas.TradeCreate):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(db: Session, ticker: str = None, start: datetime = None, end: datetime = None):
    query = db.query(models.Trade)
    if ticker:
        query = query.filter(models.Trade.ticker == ticker)
    if start:
        query = query.filter(models.Trade.timestamp >= start)
    if end:
        query = query.filter(models.Trade.timestamp <= end)
    return query.all()
