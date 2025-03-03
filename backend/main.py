from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import login, register, user_me

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'API is running'}

app.include_router(login.router, tags=['Authetication'])

app.include_router(register.router, tags=['Register'])

app.include_router(user_me.router, tags=['User'])
