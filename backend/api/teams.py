from fastapi import APIRouter, HTTPException
from api.models import ResponseTeam, ResponseTeamAccount
from db.sql import DatabaseManager
import logging 

router = APIRouter() 

sql = DatabaseManager()

@router.get('/team')
async def get_teams_async(): 
    return sql.get_teams()

@router.post('/team')
async def create_team_async(body: ResponseTeam):
    try:
        sql.create_team(body)
        return True
    except Exception as err:
        logging.error(f'Unable to create Team: {err}')
        raise HTTPException(status_code=500, detail='Unable to create team due to an unhandled exception')
    
@router.get('/team/{team_uuid}')
async def get_team_by_id_async(team_uuid: str):
    return sql.get_team_by_id(team_uuid)

@router.delete('/team/{team_uuid}')
async def delete_team_by_id_async(team_uuid: str):
    try:
        sql.delete_team_by_id(team_uuid)
        return True
    except Exception as err:
        logging.error(f'Unable to delete team: {err}')
        raise HTTPException(status_code=500, detail='Unable to delete team due to an unhandled exception')
    
@router.patch('/team/{team_uuid}')
async def update_team_async(team_uuid: str,body: ResponseTeam):
    try:
        sql.update_team_by_id(
            response_team_id=team_uuid,
            updated_information=body
            )
        return True
    except Exception as err:
        logging.error(f'Unable to update team: {err}')
        raise HTTPException(status_code=500, detail='Unable to update team due to and unhandled exception')
    

@router.post('/team/{team_uuid}/members')
async def add_team_member_async(): 
    """
    * Create an API endpoint that calls the sql.insert_team_user function in python
    * Add InsertResponseTeamUser stored procedure to the sql.py file 
    * Accept the Team_UUID within the async function definition above 
    * Accept a User_UUID using the UserAccount model from the models.py file as the body
    """
    pass 