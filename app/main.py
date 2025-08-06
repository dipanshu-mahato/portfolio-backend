from fastapi import FastAPI
from app.api.routes import api_router
from app.model import Base
from app.database import engine

# Create tables at startup if they don't exist (optional, recommended to use Alembic)
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job-Tracker API")
app.include_router(prefix='/api', router=api_router)

@app.get('/helloworld')
def hello_world():
    return 'Hello World'