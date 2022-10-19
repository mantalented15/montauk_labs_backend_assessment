from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import requests

driver = webdriver.Chrome('chromedriver')
driver.get('https://transparency-in-coverage.uhc.com/')

# time.sleep(80)
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]//div[@class="ant-space-item"]')
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]')
# a = driver.find_element(By.XPATH, '//div[@class="ant-space-item"]/a')
# a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')

# WebDriverWait(driver,240).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
# a = driver.find_element(By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')
try:
    # a = WebDriverWait(driver,180).until(EC.presence_of_element_located((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
    # a = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-testid="list-item-1"]/div/div/a')))
    a = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-testid="list-item-1"]//a')))

    href = a.get_attribute('href')
    # a = WebDriverWait(driver,180).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="ant-space-item"]/a')))
    # a = WebDriverWait(driver,180).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="ant-list-items"]')))
except:
    print("Timed out waiting for page to load")


# a_list = []
# for i in range(len(a)):
#     a_list.append(a[i].text)

# print(a.text)
# print(a.get_attribute("href"))
# print(a_list)
print(requests.get(href).text)