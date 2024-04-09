from pydantic import BaseModel 
from datetime import datetime

class UserAccount(BaseModel): 
    user_uuid: str | None = None
    user_fname: str | None = None
    user_lname: str | None = None
    created_on: None | datetime = None
    account_role_id: int | None = None
    is_active: bool | None = None