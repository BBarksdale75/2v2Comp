from fastapi import APIRouter, HTTPException
from api.models import UserAccount
from api.exceptions.AccountException import AccountNotFound
from db.sql import Accounts
import logging 

router = APIRouter() 

sql = Accounts()

@router.get('/account')
async def get_all_user_accounts_async(): 
    return sql.get_user_accounts()

@router.post('/account')
async def create_user_account_async(body: UserAccount):
    try: 
        return {"UserId": sql.create_user_account(body) } 
    except Exception as err: 
        logging.error(f'Unable to create account: {err}')
        raise HTTPException(status_code=500, detail='Unable to create user account due to an unhandled exception.') 

@router.get('/account/{user_uuid}')
async def get_user_account_by_id_async(user_uuid: str):
    try: 
        return sql.get_user_account_by_id(user_uuid)
    except AccountNotFound as err: 
        raise HTTPException(status_code=404,detail=f'User not found with Id: {user_uuid}')        

@router.delete('/account/{user_uuid}')
async def delete_user_account_async(user_uuid: str):
    try: 
        sql.delete_user_account_by_id(user_uuid)
        return 
    except Exception as err: 
        logging.error(f'Unable to delete account: {err}')
        raise HTTPException(status_code=500, detail='Unable to delete user account due to an unhandled exception.') 

@router.patch('/account/{user_uuid}')
async def update_user_account_async(user_uuid: str,body:UserAccount):
    try:
        sql.update_user_account_by_id(
            user_uuid=user_uuid,
            updated_information=body
            )
        return True
    except Exception as err: 
        logging.error(f'Unable to update account: {err}')
        raise HTTPException(status_code=500, detail='Unable to update user account due to an unhandled exception.') 