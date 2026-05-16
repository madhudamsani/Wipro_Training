import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()

def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert=driver.switch_to.alert
    assert alert.text=="I am a JS Alert","Alert test is wrong"
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result=driver.find_element(By.ID, "result").text
    assert "you successfully clicked an alert" in result,'result text is wrong'

def test_js_confirmdismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert").click()
    alert=driver.switch_to.alert
    time.sleep(3)
    assert alert.text== "I am a JS Confirm", 'Alert text was wrong'
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "you clicked :Cancel" in result, 'result text is wrong'


def test_isconfirmok(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm").click()
    alert=driver.switch_to.alert
    time.sleep(3)
    assert alert.text== "I am a JS Confirm", 'Alert text was wrong'
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "you clicked :Ok" in result, 'result text is wrong'

def test_js_(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt").click()
    alert=driver.switch_to.alert
    time.sleep(3)
    assert alert.text== "I am a JS prompt", 'Alert text was wrong'
    alert.send_keys("Python Selenium")
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "Python Selenium" in result, 'result text is wrong'


