from pydantic import BaseModel, Field, EmailStr
class UserSchema(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


    class Config:
        schema_extra={
            "example" :{
                "email":"example@gmail.com",
                "password": "ddss"

            }
        }

class PostSchema(BaseModel):
    title: str = Field(...)
    description: str = Field (...)
    author: str = Field(...)

    class Config:
        sceme_extra = {
            "example": {
                "title":"cats",
                "description": "All about cats",
                "author": "Fariza"
            }
        }
    