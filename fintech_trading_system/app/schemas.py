from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TradeBase(BaseModel):
    ticker: str = Field(..., example="AAPL")
    price: float = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    side: str = Field(..., pattern="^(buy|sell)$")


class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
