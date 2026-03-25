from fastapi import APIRouter
from backend.services.api_service import test_api

router = APIRouter()

@router.post("/api-test")
def api_test_route(req: dict):
    try:
        return test_api(req["url"], req["method"])
    except Exception as e:
        return {"error": str(e)}