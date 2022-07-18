from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: Optional[int]
    name: str
    email: EmailStr
    password: str

