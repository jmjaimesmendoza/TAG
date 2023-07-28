from uuid import UUID
from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    username: str
    name: str
    password: str


class UserOut(BaseModel):
    username: str
    name: str


class SystemUser(UserOut):
    password: str