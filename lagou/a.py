import random

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://hao123.com")

while 1:
    a_list = browser.find_elements(By.TAG_NAME, 'a')
    count = len(a_list)
    index = random.randrange(0, count)
    try:
        a_list[index].click()
    except Exception as e:
        print(e)
        pass
