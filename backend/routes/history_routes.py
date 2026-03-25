from fastapi import APIRouter
from backend.database import get_connection

router = APIRouter()

@router.get("/history")
def get_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()

    conn.close()

    return {
        "history": [
            {"id": r[0], "test": r[1], "status": r[2]}
            for r in rows
        ]
    }