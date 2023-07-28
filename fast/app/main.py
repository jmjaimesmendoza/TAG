from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.src.utils.prisma import prisma
from app.src.routers import auth
from app.src.utils.auth  import get_hashed_password

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    await prisma.connect()
    await prisma.user.create_many(
        data=[
            {
                'username': "jmjm",
                'name': "juan",
                'password': get_hashed_password("123")
            },
            {
                'username': "pp",
                'name': "pedro pascal",
                'password': get_hashed_password("pp")
            },
            {
                'username': "rch",
                'name': "rodrigo chaves",
                'password': get_hashed_password("potus1")
            },
            {
                'username': "First",
                'name': "Lion El Johnson",
                'password': get_hashed_password("legion1")
            },
            {
                'username': "Guilliman",
                'name': "Roboute",
                'password': get_hashed_password("codex")
            }
        ]
    )

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}