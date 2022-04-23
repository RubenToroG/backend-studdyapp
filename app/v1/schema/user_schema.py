from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example='email@emailexample.com'
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example='MyUsername'
    )

class User(UserBase):
    id: int = Field(
        ...,
        example="3"
    )

class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='Strong_Password'
    )