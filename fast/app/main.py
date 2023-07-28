from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.prisma import prisma
from src.routers import auth

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:5000",
]

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
            'password': "123"
        },
        {
            'username': "pp",
            'name': "pedro pascal",
            'password': "sugar"
        },
        {
            'username': "Brck",
            'name': "Barack",
            'password': "potus1"
        },
        {
            'username': "TheGrey",
            'name': "Gandalf",
            'password': "wzrd"
        },
        {
            'username': "Guilliman",
            'name': "Roboute",
            'password': "marine"
        }
        ]
    )

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}