from api.routes.account import router as accountrouter
from api.routes.teams import router as teamsrouter
from api.routes.events import router as eventsrouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(accountrouter)
app.include_router(teamsrouter)
app.include_router(eventsrouter)