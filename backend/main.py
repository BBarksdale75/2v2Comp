from api.account import router as accountrouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(accountrouter)