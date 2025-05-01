from passlib.context import CryptContext




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generete_password(first_name:str):
    return f"{first_name}123"

def hash_password(plain_password):
    return pwd_context.hash(plain_password)

def verify_password(plain_pass:str,hashed_pass:str):
    return pwd_context.verify(plain_pass,hashed_pass)

