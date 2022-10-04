from typing import List, Union
from uuid import UUID

from fastapi import FastAPI, HTTPException
from models import Gender, Roles, User, UserUpdateRequest


app = FastAPI()

db: List[User] = [
    User(id=UUID("75ecd97f-7b76-4110-b371-cfca0ab59453"), first_name="Siddhant",
         last_name="Sharma", gender=Gender.male, roles=[Roles.admin, Roles.user]),
    User(id=UUID("c1f2958d-c8de-4c40-9fcd-21a10eb7d683"), first_name="Avantika",
         last_name="Joshi", gender=Gender.female, roles=[Roles.student])
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/app/v1/users")
async def get_users():
    return db


@app.post("/app/v1/users")
def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/app/v1/users/{first_name}")
def delete_user(first_name: str):
    for user in db:
        if user.first_name == first_name:
            db.remove(user)
            return db
        raise HTTPException(
            status_code=404, detail=f"user with first_name: {first_name} does not exists")


@app.put("/app/v1/users/{user_id}")
def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user
    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exists")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
