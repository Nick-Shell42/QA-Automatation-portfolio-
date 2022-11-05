from selenium import webdriver                      
from selenium.webdriver.common.by import By
import time 

link = "https://www.degreesymbol.net/"              

try:
    browser = webdriver.Chrome() 
    browser.get(link)   
    
    time.sleep(2)
    link = browser.find_element(By.LINK_TEXT, "Degree Symbol on Compass")
    link.click()
    time.sleep(4)
   
   
finally:

    browser.quit()