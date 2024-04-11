from pydantic import BaseModel 
from datetime import datetime

class UserAccount(BaseModel): 
    user_uuid: str | None = None
    user_fname: str | None = None
    user_lname: str | None = None
    created_on: None | datetime = None
    account_role_id: int | None = None
    is_active: bool | None = None

class ResponseTeam(BaseModel):
    """
    Represents a response team.
    
    Attributes:
        response_team_id (str, optional): The ID of the response team.
        response_team_description (str, optional): The description of the response team.
        response_team_name (str, optional): The name of the response team.
    """
    response_team_id: str | None = None
    response_team_description: str | None = None
    response_team_name: str | None = None

class ResponseTeamAccount(UserAccount):
    """
    Represents a user's association with a response team.
    
    Attributes:
        user_uuid (str, optional): The UUID of the user.
        response_team_id (str, optional): The ID of the response team.
    """
    response_team_id: str | None = None