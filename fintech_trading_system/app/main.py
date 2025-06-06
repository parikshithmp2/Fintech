from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal, Base
from typing import List, Optional
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/trades", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    return crud.create_trade(db, trade)

@app.get("/trades", response_model=List[schemas.Trade])
def read_trades(ticker: Optional[str] = None, start: Optional[datetime] = None, end: Optional[datetime] = None, db: Session = Depends(get_db)):
    return crud.get_trades(db, ticker=ticker, start=start, end=end)
