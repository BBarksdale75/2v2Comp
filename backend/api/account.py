from fastapi import APIRouter, HTTPException
from api.models import UserAccount
from db.sql import DatabaseManager
import logging 

router = APIRouter() 

sql = DatabaseManager()

@router.get('/accounts')
async def get_all_user_accounts(): 
    return sql.get_user_accounts()

@router.post('/accounts')
async def create_user_account(body: UserAccount):
    try: 
        sql.create_user_account(body)
        return True
    except Exception as err: 
        logging.error(f'Unable to create account: {err}')
        raise HTTPException(status_code=500, detail='Unable to create user account due to an unahndled exception.') 

@router.get('/accounts/{user_guid}')
async def get_all_user_accounts(user_guid: str): 
    return sql.get_user_account_by_id(user_guid)

