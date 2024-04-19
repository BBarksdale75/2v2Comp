# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.account import router as accountrouter
from api.routes.teams import router as teamsrouter
from api.routes.events import router as eventsrouter

app = FastAPI()

# Define allowed origins

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE","PATCH"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include routers
app.include_router(accountrouter)
app.include_router(teamsrouter)
app.include_router(eventsrouter)
