from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import dotenv
dotenv.load_dotenv()
import os


# Password configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Tokens JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#verify password
def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

#generate token access
def create_access_token(data:dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

#Token decode
def decode_access_token(token: str):
  try:
    payload = jwt.encode(token, SECRET_KEY, algorithm=[ALGORITHM])
    return payload
  except JWTError:
    return None
