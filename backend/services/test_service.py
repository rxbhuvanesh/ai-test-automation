from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def run_all_tests():
    options = Options()

    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()

    return [{"test": "Google Page Load", "status": "Pass" if title else "Fail"}]