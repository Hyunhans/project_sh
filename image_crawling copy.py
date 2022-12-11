import unittest

from attr import Attribute
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

 

driver = webdriver.Chrome()

driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
time.sleep(50)

elem = driver.find_element(By.NAME, "q")

elem.send_keys("황금알 낳는 거위를 찾아서")

time.sleep(10)


elem.send_keys(Keys.RETURN) # 엔터키 누름

# driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[0].click()

time.sleep(10)

# print(driver.find_element(By.CSS_SELECTOR, ".rg_i.Q4LuWd").get_attribute("src"))