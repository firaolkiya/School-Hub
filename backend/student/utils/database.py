from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from ..config import setting


DATABASE_URL=f"postgresql://{setting.database_username}:{setting.database_password}@ep-divine-cloud-a4oihvs8-pooler.us-east-1.aws.neon.tech/{setting.database_name}?sslmode=require"

engine=create_engine(DATABASE_URL)


SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
    )

Base=declarative_base()

async def get_db():
    try:
        db=  SessionLocal()
        yield db
    finally:
        
        db.close()