from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("index.html")
time.sleep(2)

# Flow A
driver.find_element(By.ID, "fname").send_keys("Harsh")
driver.find_element(By.ID, "email").send_keys("harsh@test.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "gender").send_keys("Male")
driver.find_element(By.ID, "country").send_keys("India")
time.sleep(1)
driver.find_element(By.ID, "state").send_keys("Uttar Pradesh")
time.sleep(1)
driver.find_element(By.ID, "city").send_keys("Lucknow")
driver.find_element(By.ID, "password").send_keys("Harsh@123")
driver.find_element(By.ID, "cpassword").send_keys("Harsh@123")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("negative_test_error.png")

# Flow B
driver.refresh()
time.sleep(2)
driver.find_element(By.ID, "fname").send_keys("Harsh")
driver.find_element(By.ID, "lname").send_keys("Verma")
driver.find_element(By.ID, "email").send_keys("harsh@example.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "gender").send_keys("Male")
driver.find_element(By.ID, "country").send_keys("India")
time.sleep(1)
driver.find_element(By.ID, "state").send_keys("Delhi")
time.sleep(1)
driver.find_element(By.ID, "city").send_keys("New Delhi")
driver.find_element(By.ID, "password").send_keys("Harsh@123")
driver.find_element(By.ID, "cpassword").send_keys("Harsh@123")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("positive_test_success.png")

# Flow C
driver.refresh()
time.sleep(2)
driver.find_element(By.ID, "country").send_keys("India")
time.sleep(1)
driver.find_element(By.ID, "state").send_keys("Karnataka")
time.sleep(1)
driver.find_element(By.ID, "city").send_keys("Bengaluru")
driver.find_element(By.ID, "password").send_keys("Hello123!")
driver.find_element(By.ID, "cpassword").send_keys("Mismatch123!")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("logic_test_error.png")

driver.quit()
