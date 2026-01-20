from fastapi import APIRouter,HTTPException,Depends
from app.schemas import TaskCreate,TaskUpdate
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Task
from app.schemas import TaskCreate,TaskUpdate
router = APIRouter(prefix="/tasks",tags=["tasks"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/")
def create_task(payload :TaskCreate,db : Session = Depends(get_db)):
   task = Task(title= payload.title,done = False)
   db.add(task)
   db.commit()
   db.refresh(task)
   return task
    
@router.get("/")
def list_tasks(db : Session = Depends(get_db)):
    return db.query(Task).all()
@router.get("/{task_id}")
def access_id(task_id : int, db :Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404,detail="Task not found")
    return task
@router.put("/{task_id}")
def update_task(task_id : int , payload : TaskUpdate,db : Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    task.title = payload.title
    task.done = payload.done
    db.commit()
    db.refresh(task)
    return {"message" : "Task updated successfully"}
@router.delete("/{task_id}")
def delete_task(task_id : int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message" : "Task deleted successfully"}
