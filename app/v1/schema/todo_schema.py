from datetime import datetime
from turtle import title
from venv import create

from pydantic import BaseModel
from pydantic import Field


class TodoCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example='My first todo'
    )

class Todo(TodoCreate):
    id: int = Field(...)
    is_done: bool = Field(default=False)
    create_at: datetime = Field(default=datetime.now())