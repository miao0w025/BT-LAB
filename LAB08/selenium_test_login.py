import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("file:///C:/path/to/login.html")  # đổi sang path thật
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Chào mừng" in driver.page_source or "Welcome" in driver.page_source

def test_login_wrong(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Sai mật khẩu" in driver.page_source or "Invalid" in driver.page_source

def test_login_empty(driver):
    driver.find_element(By.ID, "loginBtn").click()
    assert "Vui lòng nhập" in driver.page_source or "Required" in driver.page_source
