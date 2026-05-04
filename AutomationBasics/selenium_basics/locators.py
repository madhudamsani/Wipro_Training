import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver =webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get('https://google.com')
'''
#Id
#search_input = driver.find_element(By.ID, "APjFqb")
#search_input.send_keys("selenium")
#time.sleep(3)


#Name
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys("selctors")
time.sleep(10)

#Name
google_search_button = driver.find_element(By.NAME, 'btnK')
google_search_button.click()
time.sleep(10)

#imfl_btn


#tagname
href_elemetns= driver.find_elements(By.TAG_NAME, "a")
for elmt in href_elemetns:
    print(f'{elmt.text}-{elmt.get_attribute("href")}')



#Linktext
images_link= driver.find_element(By.LINK_TEXT, "Images")
images_link.click()
sleep(5)


#partal linktext
images_link= driver.find_element(By.PARTIAL_LINK_TEXT, "ma")
images_link.click()
sleep(5)


#CSSselectors
search_input=driver.find_element(By.CSS_SELECTOR, "div > textarea")
search_input.send_keys("selenium")
sleep(5)

#Xpath
settings_text =driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div')
print(settings_text.text)
sleep(5)


# AND & OR expression
and_example = driver.find_element(By.XPATH, "")
print(f"AND Example -> Found with both conditions: {and_example.text}")

or_example = driver.find_element(By.XPATH, "")
print(f"OR Example -> Found with OR conditions: {or_example.text}")

#Child - select all 'td' elements that ate direct children of a row 
rows=driver.find_element(By.XPATH,"")
print(f"Chile Example -> found {len(rows)} columns in the first table.")

#parent - get the parent row ofa particular cell
email_cell=driver.find_element(By.XPATH, )
parent_row=driver.find_element(By.XPATH, "")
print(f"Parent Example -> Email'{email_cell.text}' belongs to row with first name:"
      f"{parent_row.find_element(By.XPATH, '')}")


#Ancestor - get the table element that is an ancestor of a cell
ancestor_table=driver.find_element(By.XPATH, "")
print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")

#Descendant - find all descendants under table body
descendants=driver.find_element(By.XPATH, "")
print(f"Descendants Example -> Found: {len(descendants)} descendant cells")
'''
#RELATIVE LOCATORS

driver.get('https://www.saucedemo.com/')
time.sleep(2)

#Elements used for reference
username_field=driver.find_element(By.ID, "user-name")
password_field=driver.find_element(By.ID, "password")
login_button=driver.find_element(By.ID, "login-button")

#above -> element located above another
label_above_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").above(password_field)
)

print(f"Above Example -> Text above password: {label_above_password.get_attribute('placeholder')}")
label_above_password.send_keys('standard_user')
time.sleep(3)

#below -> element located below another
field_below_username = driver.find_element(
    locate_with(By.TAG_NAME, "input").below(username_field)
)
print(f"Below Example -> Placeholder below username: {field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys('secret_sauce')
time.sleep(3)
login_button.click()
time.sleep(2)

#toRightof -> element to the left of another
twitter_icon=driver.find_element(By.LINK_TEXT, "Twitter")
facebook_icon=driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon))
print(f"toleftOf Example -> Element to the right of Twitter icon has href:{facebook_icon.get_attribute('href')}")

#toLeftof -> element to the right of another
left_icon=driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(facebook_icon))
print(f"toRightOf Example -> Element to the left of Facebook icon has href:{left_icon.get_attribute('href')}")

#near -> element close to another (within ~ 50px by default)
near_twitter = driver.find_element(locate_with(By.TAG_NAME, "a").near(facebook_icon))
print(f"Near Example -> Element near Facebook icon has href:{near_twitter.get_attribute('href')}")

time.sleep(2)
driver.quit()

