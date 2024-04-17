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

class EventType(BaseModel): 
    event_type_id: int  | None = None
    event_type_name: str | None = None
    event_type_description: str | None = None

class EventStatus(BaseModel): 
    event_status_id: int  | None = None
    event_status_name: str | None = None
    event_status_desc: str  | None = None

class EventModel(BaseModel):
    event_uuid: str | None = None
    event_type_id: int  | None = None
    event_name: str  | None = None
    event_status_id: int  | None = None
    commander_user_uuid: str  | None = None
    event_severity_id: int  | None = None
    created_on: datetime | None = None

class EventTimelineNote(BaseModel): 
    timeline_note_uuid: str | None = None
    timeline_uuid: str | None = None
    entry_note: str | None = None
    timeline_entry_entry_type_id: int | None = None 
    created_on: datetime | None = None

class EventTimelineEntry(BaseModel): 
    event_uuid: str | None = None 
    timeline_uuid: str | None = None 
    timeline_entry_type_id: int | None = None 
    entered_by_user_uuid: int | None = None 
    created_on: datetime | None = None

class EventTimelineEntryType(BaseModel): 
    timeline_entry_type_id: int 
    timeline_entry_type_name: str 
    timeline_entry_type_desc: str 