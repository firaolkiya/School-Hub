from fastapi.testclient import TestClient
from app.main import app
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from student.config import setting
from student.utils.database import get_db,Base

DATABASE_URL=f"postgresql://{setting.database_username}:{setting.database_password}@ep-divine-cloud-a4oihvs8-pooler.us-east-1.aws.neon.tech/{setting.database_name}_test?sslmode=require"

engine=create_engine(DATABASE_URL)


TestSessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
    )



@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        db=  TestSessionLocal()
        yield db
    finally:
        db.close()
        
@pytest.fixture
def client(session):
    async def get_test_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db]=get_test_db
    yield TestClient(app)

