from fastapi import APIRouter
from config.db import conn
from models.user import users
from fastapi import FastAPI, Depends, HTTPException
from auth.auth import AuthHandler
from schemas.user import User
from schemas.authdetail import AuthDetails

user = APIRouter()
auth_handler = AuthHandler()

@user.post('/register', status_code=201)
def register(user: User):
    new_user = {"name": user.name, "email": user.email}
    if conn.execute(users.select().where(users.c.email == user.email)).fetchall():
        raise HTTPException(status_code=400, detail='Email is taken')
    hashed_password = auth_handler.get_password_hash(user.password)
    new_user['password'] = hashed_password
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.post('/login')
def login(user: AuthDetails):
    userx = conn.execute(users.select().where(users.c.email == user.email)).first()
    
    if (userx is None) or (not auth_handler.verify_password(user.password, userx['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(userx['email'])
    return { 'token': token }