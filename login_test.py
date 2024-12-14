from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure the correct driver is installed and added to PATH
driver.maximize_window()

# Base URL of the application
base_url = "http://example.com/login"  # Replace with the actual URL

def test_valid_login():
    driver.get(base_url)
    driver.find_element(By.ID, "username").send_keys("valid_user")  # Replace with valid username
    driver.find_element(By.ID, "password").send_keys("valid_password")  # Replace with valid password
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(3)
    assert "Dashboard" in driver.title, "Valid login failed"

def test_invalid_login_username():
    driver.get(base_url)
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("valid_password")  # Replace with valid password
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(3)
    error_message = driver.find_element(By.ID, "errorMessage").text
    assert "Invalid username or password" in error_message, "Error message not displayed for invalid username"

def test_invalid_login_password():
    driver.get(base_url)
    driver.find_element(By.ID, "username").send_keys("valid_user")  # Replace with valid username
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(3)
    error_message = driver.find_element(By.ID, "errorMessage").text
    assert "Invalid username or password" in error_message, "Error message not displayed for invalid password"

# Run tests
try:
    test_valid_login()
    print("Valid login test passed.")
    test_invalid_login_username()
    print("Invalid username test passed.")
    test_invalid_login_password()
    print("Invalid password test passed.")
finally:
    driver.quit()

