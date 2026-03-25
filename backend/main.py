from fastapi import FastAPI
from backend.routes import test_routes, api_routes, history_routes
from backend.database import init_db

app = FastAPI()

init_db()  # 👈 ADD THIS

app.include_router(test_routes.router)
app.include_router(api_routes.router)
app.include_router(history_routes.router)