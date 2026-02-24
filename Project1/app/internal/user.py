from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..core.models import Users
from ..core.db import get_db
from ..schema.schema import TokenData
from ..config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
	plain_password = plain_password[:72]
	return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
	password = password[:72]
	return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Optional[Users]:
	user = db.query(Users).filter(Users.email == email).first()
	if not user:
		return None
	if not verify_password(password, user.hashed_password):
		return None
	return user

REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Users:
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email: str = payload.get("sub")
		if email is None:
			raise credentials_exception
		token_data = TokenData(email=email)
	except JWTError:
		raise credentials_exception
	user = db.query(Users).filter(Users.email == token_data.email).first()
	if user is None:
		raise credentials_exception
	return user


def get_current_active_user(current_user: Users = Depends(get_current_user)) -> Users:
	if not current_user.is_active:
		raise HTTPException(status_code=400, detail="Inactive user")
	return current_user

def get_all_user(
	db: Session =  Depends(get_db)
):
    results = db.query(Users).filter(Users.is_active == True).all()
    return results