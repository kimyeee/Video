from selenium import webdriver
from selenium.webdriver.common.by import By


def t():
    browser = webdriver.Chrome()

    browser.get("https://www.lagou.com")
    # browser.find_element_by_id('cboxClose').click()
    browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")
    ii = browser.find_elements(By.CLASS_NAME, 'position_link')
    for i in ii:
        print(i)
        i.click()


# print(browser.page_source)
t()

print('1')
