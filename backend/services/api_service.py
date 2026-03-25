import requests

def test_api(url, method):
    res = requests.request(method, url)
    return {
        "status_code": res.status_code,
        "response": res.text[:500]
    }