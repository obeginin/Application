from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    balance: float = Field(ge=0, default=0)