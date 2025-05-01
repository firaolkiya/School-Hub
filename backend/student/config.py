from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    
    class Config:
        env_file='.env'
setting = Settings()