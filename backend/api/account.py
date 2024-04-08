from fastapi import FastAPI
import psycopg2 
from models import UserAccount
import os

app = FastAPI() 

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST_NAME'),
    port=os.getenv('DB_PORT')
)

# Create a cursor object using the connection
cur = conn.cursor()

@app.get('/accounts')
async def get_all_user_accounts(): 
    cur.execute("SELECT * FROM GetAccounts();")
    result = cur.fetchall() 
    accounts = []
    for row in result: 
        accounts.append( 
            dict(zip(UserAccount.model_fields.keys(),row))
        )
    return accounts