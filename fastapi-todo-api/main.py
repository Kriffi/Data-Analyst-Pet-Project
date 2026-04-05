from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

# Инициализация приложения
app = FastAPI(
    title="Simple TODO API",
    description="CRUD операции над задачами (хранятся в памяти)",
    version="1.0.0"
)

# Модель для создания/обновления задачи (входные данные)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Модель для ответа (включает ID)
class TaskResponse(TaskCreate):
    id: UUID

# "База данных" в памяти: словарь {id: задача}
tasks_db: dict[UUID, TaskResponse] = {}

# --- Эндпоинты ---

@app.get("/", tags=["Root"])
def root():
    """Корневой эндпоинт, возвращает приветствие."""
    return {"message": "Добро пожаловать в TODO API! Используйте /docs для интерактивной документации."}

@app.get("/tasks", response_model=List[TaskResponse], tags=["Tasks"])
def get_all_tasks():
    """Получить список всех задач."""
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def get_task(task_id: UUID):
    """Получить одну задачу по её ID."""
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@app.post("/tasks", response_model=TaskResponse, status_code=201, tags=["Tasks"])
def create_task(task: TaskCreate):
    """Создать новую задачу. ID генерируется автоматически."""
    new_id = uuid4()
    new_task = TaskResponse(id=new_id, **task.dict())
    tasks_db[new_id] = new_task
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def update_task(task_id: UUID, updated_data: TaskCreate):
    """Полностью обновить существующую задачу."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    updated_task = TaskResponse(id=task_id, **updated_data.dict())
    tasks_db[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}", status_code=204, tags=["Tasks"])
def delete_task(task_id: UUID):
    """Удалить задачу по ID."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    del tasks_db[task_id]
    # 204 No Content — тело ответа пустое