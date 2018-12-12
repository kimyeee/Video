import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Spider:
    url_list = []

    def __init__(self, page_num):
        self.page_num = page_num

    def __enter__(self):
        self.browser = webdriver.Chrome()
        return self

    def login_requests(self):
        self.browser.get("https://www.lagou.com")
        self.browser.get(
            "https://passport.lagou.com/login/login.html?ts=1544578275889&serviceId=lagou&service=https%253A%252F%252Fwww.lagou.com%252F&action=login&signature=9E7D49AD751AC103148C9544368EE98F")
        # self.browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")
        self.browser.find_element(By.CLASS_NAME, 'icon_tencent').click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])
        print(self.browser.title)
        self.browser.switch_to.frame('ptlogin_iframe')
        self.browser.find_element(By.CLASS_NAME, 'img_out_focus').click()
        time.sleep(3)

        # self.browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")
        # ii = self.browser.find_elements(By.CLASS_NAME, 'position_link')
        # for i in ii:
        #     url = i.get_attribute('href')
        #     print(url)
        #     self.url_list.append(url)
        # yield url
        # i.click()
        # self.browser.switch_to.window(self.browser.window_handles[-1])
        # print(self.browser.title)
        # self.browser.close()
        # self.browser.switch_to.window(self.browser.window_handles[-1])

    def url_requests(self):
        self.browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")
        for c in range(self.page_num):
            ii = self.browser.find_elements(By.CLASS_NAME, 'position_link')
            for i in ii:
                url = i.get_attribute('href')
                print(url)
                self.url_list.append(url)
            self.browser.find_element(By.CLASS_NAME, 'pager_next ').click()

    def parse_requests(self):
        for url in self.url_list:
            print("url: ", url)
            # return
            self.browser.get(url)
            company = self.browser.find_element(By.CLASS_NAME, 'company').text
            # self.browser.close()
            print(company)

    def start(self):
        self.login_requests()
        self.url_requests()
        self.parse_requests()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()


with Spider(5) as s:
    s.start()
