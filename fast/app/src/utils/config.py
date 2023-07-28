from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str = "TAG API"    
  ACCESS_TOKEN_EXPIRE_MINUTES = 30
  ALGORITHM = "HS256"
  JWT_SECRET_KEY = 'TAG'

class Config:
    env_file = ".env"

settings = Settings()