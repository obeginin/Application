from fastapi import FastAPI, HTTPException
from models import User
from schemas import CreateUserRequest, TransferRequest
from storage import users, add_user, get_user_by_email
from service import transfer_money

app = FastAPI(title="Users and Balance API")


@app.post("/users", response_model=User)
async def create_user(user_data: CreateUserRequest):
    existing = await get_user_by_email(user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email уже существует")
    return await add_user(user_data.name, user_data.email, user_data.balance)


@app.get("/users", response_model=list[User])
async def list_users():
    return users


@app.post("/transfer")
async def transfer(transfer_data: TransferRequest):
    return await transfer_money(
        transfer_data.from_user_id,
        transfer_data.to_user_id,
        transfer_data.amount
    )