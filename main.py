from fastapi import FastAPI
from app.routers.principal import router as principal_router
from app.routers.teacher import router as teacher_router

# ✅ Create the FastAPI app instance
app = FastAPI()

# ✅ Example route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# ✅ Include routers
app.include_router(principal_router, prefix="/principal")
app.include_router(teacher_router, prefix="/teacher")
