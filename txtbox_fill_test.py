from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "https://demoqa.com/text-box"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    browser.set_window_size(1352, 715)
    input1 = browser.find_element(By.ID, "userName")
    input1.send_keys("Garry LLoyd Sniff")
    input2 = browser.find_element(By.ID, "userEmail")
    input2.send_keys("GLS@outdatedmailbox.com")
    input3 = browser.find_element(By.ID, "currentAddress")
    input3.send_keys("Russia, Moscow, 123 commonstreet, building 4, ap. 6")
    input4 = browser.find_element(By.ID, "permanentAddress")
    input4.send_keys("USA, Jersey City, New Jersey, 321 jumpstreet, bld. 4")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    button = browser.find_element(By.ID, "submit")
    button.click()
    
    
	
	
finally:
    time.sleep(5)
    browser.quit()
    
