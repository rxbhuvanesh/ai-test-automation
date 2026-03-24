from fastapi import FastAPI
from backend.ai_engine import generate_test_cases
from backend.test_runner import run_all_tests
import requests
import sqlite3

app = FastAPI()

@app.post("/generate-tests/")
def generate_tests(req: dict):
    requirement = req.get("requirement")
    return {"test_cases": generate_test_cases(requirement)}

# NEW API 👇
# @app.get("/run-tests/")
# def run_tests():
#     results = run_login_test()
#     return {"results": results}

@app.get("/run-tests/")
def run_tests():
    results = run_all_tests()
    save_results(results)
    return {"results": results}

@app.post("/api-test/")
def api_test(req: dict):
    url = req.get("url")
    method = req.get("method", "GET")

    try:
        if method == "GET":
            res = requests.get(url)
        else:
            res = requests.post(url)

        return {
            "status_code": res.status_code,
            "response": res.text[:500]
        }

    except Exception as e:
        return {"error": str(e)}

def save_results(results):
    conn = sqlite3.connect("test_history.db")
    c = conn.cursor()

    for r in results:
        c.execute("INSERT INTO results (test_name, status) VALUES (?, ?)",
                  (r["test"], r["status"]))

    conn.commit()
    conn.close()