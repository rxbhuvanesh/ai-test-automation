from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os


def run_all_tests():
    results = []

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Ensure screenshot folder exists
    os.makedirs("backend/screenshots", exist_ok=True)

    test_cases = [
        {"name": "Valid Login", "username": "tomsmith", "password": "SuperSecretPassword!"},
        {"name": "Invalid Login", "username": "tomsmith", "password": "wrongpass"},
        {"name": "Empty Fields", "username": "", "password": ""}
    ]

    for test in test_cases:
        try:
            driver.get("https://the-internet.herokuapp.com/login")

            username = driver.find_element(By.ID, "username")
            password = driver.find_element(By.ID, "password")

            username.clear()
            password.clear()

            username.send_keys(test["username"])
            password.send_keys(test["password"])
            password.send_keys(Keys.RETURN)

            time.sleep(2)

            if test["name"] == "Valid Login" and "secure" in driver.current_url:
                results.append({"test": test["name"], "status": "Pass"})

            elif test["name"] != "Valid Login" and "secure" not in driver.current_url:
                results.append({"test": test["name"], "status": "Pass"})

            else:
                # 📸 Screenshot on failure
                path = f"backend/screenshots/{test['name'].replace(' ', '_')}.png"
                driver.save_screenshot(path)

                results.append({
                    "test": test["name"],
                    "status": "Fail",
                    "screenshot": path
                })

        except Exception as e:
            results.append({"test": test["name"], "status": f"Error: {e}"})

    driver.quit()
    return results