from fastapi import APIRouter, HTTPException
from api.models import ResponseTeam, ResponseTeamAccount, UserAccount
from db.sql import Teams
import logging 

router = APIRouter() 

team_handler = Teams()

@router.get('/team')
async def get_teams_async(): 
    return team_handler.get_teams()

@router.post('/team')
async def create_team_async(body: ResponseTeam):
    try:
        team_handler.create_team(body)
        return True
    except Exception as err:
        logging.error(f'Unable to create Team: {err}')
        raise HTTPException(status_code=500, detail='Unable to create team due to an unhandled exception')
    
@router.get('/team/{team_uuid}')
async def get_team_by_id_async(team_uuid: str):
    return team_handler.get_team_by_id(team_uuid)

@router.delete('/team/{team_uuid}')
async def delete_team_by_id_async(team_uuid: str):
    try:
        team_handler.delete_team_by_id(team_uuid)
        return True
    except Exception as err:
        logging.error(f'Unable to delete team: {err}')
        raise HTTPException(status_code=500, detail='Unable to delete team due to an unhandled exception')
    
@router.patch('/team/{team_uuid}')
async def update_team_async(team_uuid: str,body: ResponseTeam):
    try:
        team_handler.update_team_by_id(
            response_team_id=team_uuid,
            updated_information=body
            )
        return True
    except Exception as err:
        logging.error(f'Unable to update team: {err}')
        raise HTTPException(status_code=500, detail='Unable to update team due to and unhandled exception')
    
@router.post('/team/{team_uuid}/user')
async def create_team_user_async(team_uuid: str, body:UserAccount):
    try:
        team_handler.insert_team_user(
            team_uuid=team_uuid,
            user_uuid=body.user_uuid
        )
        return True
    except Exception as err:
        logging.error(f'Unable to insert team member: {err}')
        raise HTTPException(status_code=500, detail='Unable to insert team member due to an unhandled exception')


@router.delete('/team/{team_uuid}/member/{user_uuid}')
async def delete_team_user_async(team_uuid: str, user_uuid: str): 
    try:
        team_handler.delete_team_user(
            team_uuid=team_uuid,
            user_uuid=user_uuid
        )
        return True
    except Exception as err:
        logging.error(f'Unable to insert team member: {err}')
        raise HTTPException(status_code=500, detail='Unable to insert team member due to an unhandled exception')
