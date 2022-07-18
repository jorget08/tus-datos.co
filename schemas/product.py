from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from datetime import date

class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float

class UpdateProduct(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]