import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)



#text input
text_input=driver.find_element(By.ID, 'my-text-id')
text_input.clear()
text_input.send_keys("selenium webdriver demo")


#password input

password_input= driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")


#textarea
textarea_input=driver.find_element(By.NAME, "my-textarea")
textarea_input.clear()
textarea_input.send_keys("this is a sample text")

#checkbox
checkbox=driver.find_element(By.ID, "my-check-2")
checkbox.click()

#radio
radio=driver.find_element(By.ID, "my-radio-2")
radio.click()

#dropdown
dropdown=driver.find_element(By.NAME, "my-select")
dropdown.click()
option=driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2'] ")
option.click()

#multiselect
multiselect=driver.find_element(By.NAME, "my-datalist")
multiselect.send_keys("New York")

#file upload
file_upload= driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\\Wipro Training\\AutomationBasics\\selenium_basics\\locators.py")

#range slider
slider=driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value=9;", slider)


#color picker
color=driver.find_element(By.NAME, 'my-colors')
color.send_keys('#00ff00')


#date picker
date=driver.find_element(By.NAME, "my-date")
date.send_keys("2025-12-28")

#submit button
submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(10)
submit.click()

time.sleep(7)
driver.quit()