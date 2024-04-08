from fastapi import FastAPI, HTTPException
from models import UserAccount
from sql import DatabaseManager
from uuid import UUID
import logging 

app = FastAPI() 

sql = DatabaseManager()

@app.get('/accounts')
async def get_all_user_accounts(): 
    return sql.get_user_accounts()

@app.post('/accounts')
async def create_user_account(body: UserAccount):
    try: 
        sql.create_user_account(body)
        return True
    except Exception as err: 
        logging.error(f'Unable to create account: {err}')
        raise HTTPException(status_code=500, detail='Unable to create user account due to an unahndled exception.') 

@app.get('/accounts/{user_guid}')
async def get_all_user_accounts(user_guid: UUID): 
    return sql.get_user_account_by_id(user_guid)

