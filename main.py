from fastapi import FastAPI, Body, Depends 
from app.model import *
from app.auth.handler import signJWT
from app.auth.bearer import Bearer
app = FastAPI()
users = []
post = [
    {
        "title":"cats",
        "description":"all about cats"
    }
]
@app.get("/")
def root():
    return{"message":"Hello world"}

def verify_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False



@app.post("/user/signup")
def create_user(user:UserSchema= Body(...)):
    users.append(user)
    return signJWT(user.email)

@app.post("/user/signin")
def login_user(user:UserLoginSchema=Body(...)):
     if verify_user(user):
         return signJWT(user.email)
     return {"error": "Invalid credentials :("}

@app.get("/")
def root():
    return {"message": "Hello World"}

def verify_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.get("/posts")
def get_posts():
    return get_posts

@app.post("/posts", dependencies=[Depends(Bearer())])
def create_post(post: PostSchema = Body(...)):
    posts.append(post)
    return post

@app.post("/user/signup")
def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)

@app.post("/user/signin")
def login_user(user: UserLoginSchema = Body(...)):
    if verify_user(user):
        return signJWT(user.email)
    return {"error": "Invalid credentials :("}