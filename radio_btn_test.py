from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "https://demoqa.com/radio-button"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    browser.set_window_size(1352, 715)
    button = browser.find_element(By.CLASS_NAME, "custom-control-label")
    button.click()
    time.sleep(2)
    
    button = browser.find_element(By.XPATH, "//div/label[@for='impressiveRadio']")
    button.click()
    time.sleep(2)
    
	
	
finally:
    time.sleep(5)
    browser.quit()
    
