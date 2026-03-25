from fastapi import APIRouter
from backend.services.test_service import run_all_tests

router = APIRouter()

@router.get("/run-tests")
def run_tests_api():
    results = run_all_tests()
    return {"results": results}