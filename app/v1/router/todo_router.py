from fastapi import APIRouter, Depends, Body
from fastapi import status

from app.v1.schema import todo_schema
from app.v1.service import todo_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix='/api/v1/todo')

@router.post (
    '/',
    tags=['to-do'],
    status_code=status.HTTP_201_CREATED,
    response_model=todo_schema.Todo,
    dependencies=[Depends(get_db)]
)
def create_task(
    todo: todo_schema.TodoCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return todo_service.create_task(todo, current_user)