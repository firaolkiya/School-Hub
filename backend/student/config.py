from pydantic_settings import BaseSettings,SettingsConfigDict
import cloudinary


class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(env_file=".env")

    database_password:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    database_name:str
    postgres_password:str 
    cloudinary_api_key:str
    cloudinary_secret_key:str
    cloudinary_name:str
    

setting = Settings()

cloudinary.config( 
  cloud_name = setting.cloudinary_name, 
  api_key = setting.cloudinary_api_key, 
  api_secret = setting.cloudinary_secret_key,
  secure = True
)