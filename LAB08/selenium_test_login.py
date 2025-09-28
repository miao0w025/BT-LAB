from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ASUS/Documents/CONG%20NGHE%20PHAN%20MEM/login.html")

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123")
    driver.find_element(By.ID, "loginBtn").click()

    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text

    if "Đăng nhập thành công" in msg:
        print("✅ PASS: Login thành công")
    else:
        print("❌ FAIL: Login thành công")

    driver.quit()


def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ASUS/Documents/CONG%20NGHE%20PHAN%20MEM/login.html")

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("sai-mat-khau")
    driver.find_element(By.ID, "loginBtn").click()

    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text

    if "Sai tên đăng nhập hoặc mật khẩu" in msg:
        print("✅ PASS: Sai mật khẩu báo lỗi đúng")
    else:
        print("❌ FAIL: Sai mật khẩu không báo lỗi")

    driver.quit()


def test_login_empty():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/ASUS/Documents/CONG%20NGHE%20PHAN%20MEM/login.html")

    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)

    msg = driver.find_element(By.ID, "message").text
    if "Vui lòng nhập đầy đủ thông tin" in msg:
        print("✅ PASS: Empty input báo lỗi đúng")
    else:
        print("❌ FAIL: Empty input không báo lỗi")

    driver.quit()


# chạy test
test_login_success()
test_login_wrong_password()
test_login_empty()
