from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://transparency-in-coverage.uhc.com/')

time.sleep(80)
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]//div[@class="ant-space-item"]')
# a = driver.find_elements_by_xpath('//li[@data-testid="list-item-8"]')
a = driver.find_element(By.XPATH, '//a[@href="https://uhc-tic-mrf.azureedge.net/public-mrf/2022-10-01/2022-10-01_-Big-Valley-Construction-LLC_index.json"]')
# a_list = []
# for i in range(len(a)):
#     a_list.append(a[i].text)

print(a.text)
# print(a_list)