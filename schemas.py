from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    balance: float = Field(ge=0, default=0)


class TransferRequest(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float = Field(gt=0)