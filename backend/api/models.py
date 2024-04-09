from pydantic import BaseModel 
from datetime import datetime

class UserAccount(BaseModel): 
    user_uuid: str | None
    user_fname: str 
    user_lname: str 
    created_on: None | datetime = None
    account_role_id: int 
    is_active: bool