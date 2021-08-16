from config.database import DatabaseConnection
from schema.user import User, UserCreate
from random import randint

def get_user(user_id: int):
    with DatabaseConnection() as db:
        db.execute("Select * From User Where User_Id = ?", (user_id, ))
        return db.fetchone()

def get_users():
    with DatabaseConnection() as db:
        db.execute("Select * From User")
        return db.fetchall()

def add_user(user: UserCreate):
    with DatabaseConnection() as db:
        user_id = randint(10000000, 99999999)
        db.execute("Insert into User Values(?,?,?)", (user_id, user.Email, user.Name))
        return user_id


