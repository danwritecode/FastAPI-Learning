from config.database import DatabaseConnection
from schema.user import User

def get_user(user_id: int):
    with DatabaseConnection() as db:
        db.execute("Select * From User Where User_Id = ?", (user_id, ))
        return db.fetchone()



