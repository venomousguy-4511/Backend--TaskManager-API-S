from fastapi import FastAPI
from app.routes.tasks import router as tasks_router
from app.db import Base,engine
from app.models import Task
app = FastAPI()
@app.get("/db-check")
def db_check():
    try:
        conn = engine.connect()
        conn.close()
        return "Database connected successfully"
    except Exception as e:
        return"Not connected"
Base.metadata.create_all(bind=engine)

app.include_router(tasks_router)
