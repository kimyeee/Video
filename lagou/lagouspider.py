import time
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from lagou.models import Lagou
from lagou.redis_server import redis_client


class LagouSpider:
    url_list = []
    filter_fields = ['px', 'city']
    filter_fields_dict = {}

    def __init__(self, page_num, fields='Python', **kwargs):
        for field, value in kwargs.items():
            if field not in self.filter_fields:
                raise ValueError('error')
            self.filter_fields_dict[field] = value
        self.page_num = page_num
        self.fields = fields
        engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test", max_overflow=5)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.browser = webdriver.Chrome()

    def __enter__(self):
        return self

    def login_requests(self):
        self.browser.get("https://passport.lagou.com/login/login.html")
        self.browser.find_element(By.CLASS_NAME, 'icon_tencent').click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        print(self.browser.title)
        self.browser.switch_to.frame('ptlogin_iframe')
        self.browser.find_element(By.CLASS_NAME, 'img_out_focus').click()
        time.sleep(2)

    def url_requests(self):
        url = 'https://www.lagou.com/jobs/list_%s?' % self.fields
        for field, value in self.filter_fields_dict.items():
            url += '%s=%s&' % (field, value)
        url += '#order'
        # self.browser.get("https://www.lagou.com/jobs/list_%s?px=new&city=%E6%AD%A6%E6%B1%89#order")
        self.browser.get(url)
        for c in range(self.page_num):
            ii = self.browser.find_elements(By.CLASS_NAME, 'position_link')
            for i in ii:
                url = i.get_attribute('href')
                print(url)
                self.url_list.append(url)
            self.browser.find_element(By.CLASS_NAME, 'pager_next ').click()
            time.sleep(5)

    def parse_requests(self):
        for url in self.url_list:
            if redis_client.get_instance(url):
                continue
            self.browser.get(url)
            self.content_parse(self.browser.page_source)
            time.sleep(1)
            print(self.browser.title)
            redis_client.set_instance(url.rsplit('/')[-1][:-5], url)

    def content_parse(self, page_source):
        soup = bs4.BeautifulSoup(page_source)
        company = soup.find('h2', class_='fl').text.strip().split('\n')[0]
        name = soup.find('span', class_='name').text
        release = soup.find('dd', class_='job_request').text.strip().split('\n\n\n\n')
        job_request = release[0].split('\n')
        salary = job_request[0]
        city = job_request[1][1:-1]
        experience = job_request[2][:-1]
        education = job_request[3][:-1]
        job_type = job_request[4]
        release_time = release[-1].split('\n\n')[-1]
        labels = release[1].split('\n\n')[0].replace('\n', ',')
        advantage = soup.find('dd', class_='job-advantage').text.strip().split('\n')[1]
        description = soup.find('dd', class_='job_bt').text.strip()
        address = soup.find('div', class_='work_addr').text.replace(' ', '').replace('\n', '')[:-4]
        publisher = soup.find('input', class_='hr_name').get('value')
        hr_position = soup.find('input', class_='hr_position').get('value')
        aspiration = soup.find('span', class_='data').text

        company_re = soup.find('ul', class_='c_feature').contents
        domain = company_re[1].text.strip().split('\n')[0]
        phase = company_re[3].text.strip().split('\n')[0]
        scale = company_re[-4].text.strip().split('\n')[0]
        home_page = company_re[-2].text.strip().split('\n')[0]
        lagou_dict = {'company': company, 'salary': salary, 'name': name, 'city': city, 'experience': experience,
                      'education': education, 'job_type': job_type, 'release_time': release_time, 'labels': labels,
                      'advantage': advantage, 'description': description, 'address': address, 'publisher': publisher,
                      'hr_position': hr_position, 'aspiration': aspiration, 'domain': domain, 'phase': phase,
                      'scale': scale, 'home_page': home_page, }
        if len(company_re) == 11:
            investment = company_re[5].text.strip().split('\n')[0]
            lagou_dict['investment'] = investment

        obj = Lagou(**lagou_dict)
        self.session.add(obj)
        self.session.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        # self.browser.quit()

    def start(self):
        self.login_requests()
        self.url_requests()
        self.parse_requests()


if __name__ == '__main__':
    with LagouSpider(5, px='new', city='武汉') as s:
        s.start()
