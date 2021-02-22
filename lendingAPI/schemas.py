from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class userSchema(BaseModel):
    user_id : str
    
class productSchema(BaseModel):
    idf : Optional[int] = None
    user_id : str
    product_id: str
    date: date
    amount: float
    status: str
    class Config:
        orm_mode = True

class investorQuery(BaseModel):
    product_id : int
    idf : Optional[int] = None

class investorUpdate(BaseModel):
    investor_name: str
    sold: float
    
class investorSchema(BaseModel):
    idf : Optional[int] = None
    name : str
    class Config:
        orm_mode = True
        
class investorInfoSchema(BaseModel):
    idf : Optional[int] = None
    product_id : Optional[str] = None
    investor_name: str
    sold: float
    purchased: Optional[int] = None
    left_amount: Optional[float] = None
    remaining: Optional[int] = None
    class Config:
        orm_mode = True