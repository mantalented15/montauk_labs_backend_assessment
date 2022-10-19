from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://transparency-in-coverage.uhc.com/')

# time.sleep(80)
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]//div[@class="ant-space-item"]')
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]')
# a = driver.find_element(By.XPATH, '//div[@class="ant-space-item"]/a')
# a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')

WebDriverWait(driver,240).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')

# a_list = []
# for i in range(len(a)):
#     a_list.append(a[i].text)

print(a.text)
# print(a_list)