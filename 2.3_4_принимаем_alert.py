from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.ID, ("input_value")).text)
    num = str(math.log(abs(12*math.sin(x))))
    browser.find_element(By.ID, "answer").send_keys(num)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(10)
    browser.quit()
