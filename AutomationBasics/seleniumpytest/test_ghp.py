import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check


@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle =driver.title
    assert pagetitle=='Google', 'Google home page not loaded'


def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert pagetitle=='Google Images', 'Google images page not loaded'



def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains('Business'))
    #assert 'business' in driver.title.lower(), 'Business page not loaded - title check'
    #assert 'business' in driver.current_url, 'Business page not loaded - url check'
    check.equal(driver.title.lower(), 'business', 'Business page not loaded - title check')
    check.is_in('business', driver.current_url, 'Business page not loaded - url check')
