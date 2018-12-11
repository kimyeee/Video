import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Spider:
    url_list = []

    def __enter__(self):
        self.browser = webdriver.Chrome()
        return self

    # def start(self):
    #     for i in self.start_requests():
    #         self.parse(i)

    def start_requests(self):
        self.browser.get("https://www.lagou.com")
        input('>>>')
        # while 1:
        #     time.sleep(2)
        #     flag = self.browser.find_elements(By.CLASS_NAME, 'unick bl')
        #     url = self.browser.current_url
        #     if flag and url == 'https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#filterBox':
        #         break
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")
        ii = self.browser.find_elements(By.CLASS_NAME, 'position_link')
        for i in ii:
            # url = i.get_attribute('href')
            # # print(url)
            # self.url_list.append(url)
            # yield url
            i.click()

    # def parse(self, url):
    #     print("url: ", url)
    #     # return
    #     self.browser.get(url)
    #     company = browser.find_element(By.CLASS_NAME, 'company').text
    #     browser.close()
    #     print(company)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()


with Spider() as s:
    s.start_requests()
