from typing import List, Optional
from models import User
import asyncio

# Имитируем базу данных в памяти
users: List[User] = []
user_id_counter = 1


lock = asyncio.Lock()


async def add_user(name: str, email: str, balance: float) -> User:
    global user_id_counter
    async with lock:
        new_user = User(id=user_id_counter, name=name, email=email, balance=balance)
        users.append(new_user)
        user_id_counter += 1
    return new_user


async def get_user_by_id(user_id: int) -> Optional[User]:
    async with lock:
        return next((u for u in users if u.id == user_id), None)


async def get_user_by_email(email: str) -> Optional[User]:
    async with lock:
        return next((u for u in users if u.email == email), None)


async def list_all_users() -> List[User]:
    async with lock:
        return users.copy()