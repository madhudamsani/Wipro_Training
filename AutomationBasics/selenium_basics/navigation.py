import time

from selenium_basics.google_homepage_test import driver

driver.get('https://www.google.com')
time.sleep(3)

driver.get("https://www.wikipedia.com/")
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()
