from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from backend.database import get_connection   # ✅ ADD THIS

def run_all_tests():
    options = Options()

    # 🔥 REQUIRED FOR EC2
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()

    # ✅ Prepare result
    status = "Pass" if title else "Fail"
    test_name = "Google Page Load"

    # ✅ INSERT INTO DATABASE (THIS IS WHAT YOU ASKED)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO results (test_name, status) VALUES (?, ?)",
        (test_name, status)
    )

    conn.commit()
    conn.close()

    return [
        {"test": test_name, "status": status}
    ]