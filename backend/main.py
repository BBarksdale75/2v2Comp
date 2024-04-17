from api.account import router as accountrouter
from api.teams import router as teamsrouter
from api.events import router as eventsrouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(accountrouter)
app.include_router(teamsrouter)
app.include_router(eventsrouter)