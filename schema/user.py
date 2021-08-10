from pydantic import BaseModel

class User(BaseModel):
    User_Id: int
    Email: str
    Name: str

    def titlefi_name(self):
        self.Name = self.Name.title()