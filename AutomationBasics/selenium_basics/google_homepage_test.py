from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import  EdgeChromiumDriverManager


browser = input('What browser do you want to use? ')

match(browser.lower()):
    case 'chrome':
        driver =webdriver.Chrome()
    case 'edge':
        driver = webdriver.Edge()
    case _:
        print('Unknown browser - Not availabel \n Executing with default CHROME browser')
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))





'''
driver= webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get('https://www.google.com')

pagetitle=driver.title

if pagetitle=='Google':
    print('Google Homepage loaded - Pass')
else:
    print('Google Homepage Not loaded- Fail')
    
sleep(3)
    
driver.quit()
'''