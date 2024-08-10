from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import personagen_routers
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "https://angular-fighting-games.vercel.app/"
]

@app.get('/')
async def root():
    return "Olá mundo"

app.include_router(personagen_routers.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)