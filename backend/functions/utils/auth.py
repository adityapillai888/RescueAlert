import bcrypt
import jwt
from datetime import datetime, timedelta

access_token_expire_minutes=30
sectret_key='your_secret_key'
algorithm='HS256'




def hash_password(password: str) -> str:
    salt=bcrypt.gensalt()
    hashed=bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_access_token(data: dict, expires_delta: timedelta=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow() + expires_delta
    else:
        expire=datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, sectret_key, algorithm=algorithm)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload=jwt.decode(token, sectret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTError:
        return None
    
# Example usage:
# has=hash_password("hello")
# print(has)
# print(verify_password("hello", has))