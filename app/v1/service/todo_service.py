from fastapi import HTTPException, status

from app.v1.schema import todo_schema
from app.v1.schema import user_schema
from app.v1.model.todo_model import Todo as TodoModel


def create_task(task: todo_schema.TodoCreate, user: user_schema.User):

    db_task = TodoModel(
        title=task.title,
        user_id=user.id
    )
    
    db_task.save()

    return todo_schema.Todo(
        id = db_task.id,
        title = db_task.title,
        is_done = db_task.is_done,
        create_at = db_task.create_at
    )