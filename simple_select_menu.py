from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 


link = "https://demoqa.com/select-menu"

try:
    time.sleep(1)
    browser = webdriver.Chrome()
    browser.get(link)
    select1 = Select(browser.find_element (By.ID, "oldSelectMenu"))
    select1. select_by_value ("2")
    result = browser.find_element (By.CSS_SELECTOR, 'option[value = "2"]')
    fin_result = result.get_attribute ("value")
    print(fin_result)
    assert "2" == fin_result
    print ("Test passed")
    
finally:
    time.sleep(3)
    browser.quit()
    
