import time
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from lagou.models import Lagou, Comment
from lagou.redis_server import redis_client


class LagouSpider:

    def __init__(self, num):
        self.num = num
        engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test", max_overflow=5)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.browser = webdriver.Chrome()

    def __enter__(self):
        return self

    def parse_requests(self):
        url = 'https://weibo.com/3900547418/H7OBqhPF5?filter=hot&root_comment_id=0&type=comment#_rnd1545204200531'
        self.browser.get(url)
        time.sleep(15)
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        time.sleep(2)
        self.browser.execute_script(js)
        time.sleep(2)
        self.browser.execute_script(js)
        time.sleep(2)
        for url in range(self.num):
            self.browser.execute_script(js)
            time.sleep(1)
            try:
                self.browser.find_element(By.CLASS_NAME, 'more_txt').click()
            except:
                break

        while 1:
            # try:
            #     content1 = self.browser.find_elements(By.CLASS_NAME, 'WB_text')
            #     for cont in content1:
            #         if cont.text.endswith('条回复'):
            #             print(cont.text)
            #             cont.click()
            #             time.sleep(0.5)
            # except Exception as e:
            #     print(e)
            #
            # # while 1:
            try:
                content2 = self.browser.find_elements(By.TAG_NAME, 'a')
                for cont in content2:
                    if cont.text.endswith('条回复'):
                        print(cont.text)
                        cont.click()
                        time.sleep(0.5)
            except Exception as e:
                print(e)
            # if not content1 and not content2:
                break

        i = 0
        content = self.browser.find_elements(By.CLASS_NAME, 'WB_text')
        a = len(content)
        for c in content:
            i += 1
            if c.text.endswith('回复'):
                continue
            obj = Comment(content=c.text)
            self.session.add(obj)
            if i % 20 == 0:
                self.session.commit()
                print('%s/%s' % (i, a))
        self.session.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        # self.browser.quit()

    def start(self):
        self.parse_requests()


if __name__ == '__main__':
    with LagouSpider(500) as s:
        s.start()
