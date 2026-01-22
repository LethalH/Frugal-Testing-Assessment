from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


# -------------------------
# SETUP
# -------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# Open your form (update path if needed)
driver.get("file:///C:/Users/harsh/Downloads/RegistrationForm/index.html")

print("PAGE URL:", driver.current_url)
print("PAGE TITLE:", driver.title)

time.sleep(2)


# Helper to capture screenshot
def take_screenshot(name):
    driver.save_screenshot(name)
    print(f"Screenshot saved:", name)


# -------------------------
# FUNCTION TO FILL FORM
# -------------------------
def fill_form(first, last, email, phone, age, gender, address, country, state, city, password, confirm, terms):
    
    # First Name
    driver.find_element(By.ID, "fname").clear()
    driver.find_element(By.ID, "fname").send_keys(first)

    # Last Name
    driver.find_element(By.ID, "lname").clear()
    if last != "":
        driver.find_element(By.ID, "lname").send_keys(last)

    # Email
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email)

    # Phone
    driver.find_element(By.ID, "phone").clear()
    driver.find_element(By.ID, "phone").send_keys(phone)

    # Age
    driver.find_element(By.ID, "age").clear()
    if age != "":
        driver.find_element(By.ID, "age").send_keys(age)

    # Gender
    if gender.lower() == "male":
        driver.find_element(By.XPATH, "//input[@value='Male']").click()
    elif gender.lower() == "female":
        driver.find_element(By.XPATH, "//input[@value='Female']").click()
    else:
        driver.find_element(By.XPATH, "//input[@value='Other']").click()

    # Address
    driver.find_element(By.ID, "address").clear()
    driver.find_element(By.ID, "address").send_keys(address)

    # Country
    driver.find_element(By.ID, "country").send_keys(country)

    time.sleep(1)

    # State
    driver.find_element(By.ID, "state").send_keys(state)

    time.sleep(1)

    # City
    driver.find_element(By.ID, "city").send_keys(city)

    # Password
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    # Confirm Password
    driver.find_element(By.ID, "cpassword").clear()
    driver.find_element(By.ID, "cpassword").send_keys(confirm)

    # Terms & Conditions
    checkbox = driver.find_element(By.ID, "terms")
    if terms:
        if not checkbox.is_selected():
            checkbox.click()
    else:
        if checkbox.is_selected():
            checkbox.click()


# -----------------------------------------------------------------------------------------
# FLOW A — NEGATIVE TEST
# -----------------------------------------------------------------------------------------

print("\n--- FLOW A: NEGATIVE TEST (Missing Last Name) ---")

fill_form(
    first="Harsh",
    last="",                         # ❌ Last name skipped
    email="harsh@gmail.com",
    phone="912345678901",
    age="22",
    gender="Male",
    address="Gomti Nagar, Lucknow",
    country="India",
    state="Uttar Pradesh",
    city="Lucknow",
    password="Harsh@123",
    confirm="Harsh@123",
    terms=True
)

# Click Submit
driver.find_element(By.ID, "submitBtn").click()

time.sleep(1)

# Validate Last Name Error
lname_error = driver.find_element(By.ID, "lnameError").text
assert lname_error != "", "❌ ERROR: Missing Last Name NOT detected!"

print("✔ Last name error displayed:", lname_error)

take_screenshot("error-state.png")


# -----------------------------------------------------------------------------------------
# FLOW B — POSITIVE TEST
# -----------------------------------------------------------------------------------------

print("\n--- FLOW B: POSITIVE TEST ---")

# Reset by refreshing page
driver.refresh()
time.sleep(2)

fill_form(
    first="Harsh",
    last="Verma",
    email="harshverma@gmail.com",
    phone="912345678901",
    age="22",
    gender="Male",
    address="AKGEC, Ghaziabad",
    country="India",
    state="Uttar Pradesh",
    city="Noida",
    password="Harsh@123",
    confirm="Harsh@123",
    terms=True
)

# Submit
driver.find_element(By.ID, "submitBtn").click()
time.sleep(1)

# Success Message Validation
success_message = driver.find_element(By.ID, "topAlert").text
assert "Successful" in success_message, "❌ ERROR: Success message not shown!"

print("✔ Success message:", success_message)

take_screenshot("success-state.png")

# Verify form reset
assert driver.find_element(By.ID, "fname").get_attribute("value") == "", "❌ Form did NOT reset!"
assert driver.find_element(By.ID, "lname").get_attribute("value") == "", "❌ Form did NOT reset!"
assert driver.find_element(By.ID, "email").get_attribute("value") == "", "❌ Form did NOT reset!"


# -----------------------------------------------------------
# FLOW C — LOGIC VALIDATION
# -----------------------------------------------------------
print("\n--- FLOW C: LOGIC TESTING ---")

driver.refresh()
time.sleep(2)

# 1) COUNTRY → STATES UPDATE
driver.find_element(By.ID, "country").send_keys("India")
time.sleep(1)

states = driver.find_elements(By.XPATH, "//select[@id='state']/option")
assert len(states) > 0, "❌ STATES NOT LOADED AFTER COUNTRY CHANGE"
print("✔ States updated when country changed")

# 2) STATE → CITIES UPDATE
driver.find_element(By.ID, "state").send_keys("Uttar Pradesh")
time.sleep(1)

cities = driver.find_elements(By.XPATH, "//select[@id='city']/option")
assert len(cities) > 0, "❌ CITIES NOT LOADED AFTER STATE CHANGE"
print("✔ Cities updated when state changed")

# 3) PASSWORD STRENGTH VALIDATION
driver.find_element(By.ID, "password").send_keys("abc")
time.sleep(1)

strength = driver.find_element(By.ID, "passStrength").text
assert strength == "Weak", "❌ Password strength incorrect!"
print("✔ Password strength validated:", strength)

# 4) WRONG CONFIRM PASSWORD ERROR
driver.find_element(By.ID, "cpassword").send_keys("xyz")
time.sleep(1)

pass_error = driver.find_element(By.ID, "passError").text
assert pass_error != "", "❌ WRONG CONFIRM PASSWORD ERROR NOT DETECTED"
print("✔ Confirm password mismatch detected")

# 5) SUBMIT BUTTON DISABLED WHEN FORM INVALID
submit_btn = driver.find_element(By.ID, "submitBtn")
assert submit_btn.is_enabled() == False, "❌ SUBMIT BUTTON SHOULD BE DISABLED"
print("✔ Submit button disabled until form becomes valid")

print("\n--- ALL TESTS PASSED SUCCESSFULLY ✔✔✔ ---")

driver.quit()