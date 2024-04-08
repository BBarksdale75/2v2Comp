from pydantic import BaseModel 
from uuid import UUID
from datetime import datetime

class UserAccount(BaseModel): 
    user_uuid: UUID
    user_fname: str 
    user_lname: str 
    crated_on: datetime
    account_role_id: int 
    is_active: bool