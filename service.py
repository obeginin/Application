from fastapi import HTTPException
from storage import get_user_by_id


async def transfer_money(from_user_id: int, to_user_id: int, amount: float):
    if from_user_id == to_user_id:
        raise HTTPException(status_code=400, detail="Нельзя переводить самому себе")

    from_user = await get_user_by_id(from_user_id)
    to_user = await get_user_by_id(to_user_id)

    if not from_user or not to_user:
        raise HTTPException(status_code=404, detail="Один из пользователей не найден")

    if from_user.balance < amount:
        raise HTTPException(status_code=400, detail="Недостаточно средств")

    # Выполняем перевод
    from_user.balance -= amount
    to_user.balance += amount
    return {"message": "Перевод выполнен успешно"}
