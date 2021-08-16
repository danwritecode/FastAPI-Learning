from os import stat
from typing import List, Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    User_Id: int
    Email: EmailStr
    Name: str
    Wacky_Name: Optional[str]

    def titlefi_name(self):
        self.Name = self.Name.title()
    
    def add_wacky_name(self, wacky_name):
        self.Wacky_Name = wacky_name


class UserCreate(BaseModel):
    Email: EmailStr
    Name: str


class UsersResponse(BaseModel):
    Count: int
    Users: List[User]

    def wackify_user_names(self):
        for user in self.Users:
            user_dict = user.__dict__
            user.add_wacky_name(f'WACKY VERSION OF {user_dict["Name"]}')

