from pydantic_settings import BaseSettings,SettingsConfigDict



class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(env_file=".env")

    database_password:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    database_name:str
    postgres_password:str
    

setting = Settings()