import bs4
from selenium import webdriver
# from .models import Lagou

browser = webdriver.Chrome()

browser.get("https://www.lagou.com/jobs/3448313.html")


def content_parse(page_source):
    soup = bs4.BeautifulSoup(page_source)
    print(soup.find('a'))
    company = soup.find('h2', class_='fl').text.strip().split('\n')[0]
    name = soup.find('span', class_='name').text

    release = soup.find('dd', class_='job_request').text.strip().split('\n\n\n\n')
    job_request = release[0].split('\n')
    salary = job_request[0]
    # salary =salary_tag.text
    city = job_request[1][1:-1]
    experience = job_request[2][:-1]
    education = job_request[3][:-1]
    job_type = job_request[4]
    release_time = release[1].split('\n\n')[1]
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
    lagou_dict = {'company': company,
                  'salary': salary,
                  'name': name,
                  'city': city,
                  'experience': experience,
                  'education': education,
                  'job_type': job_type,
                  'release_time': release_time,
                  'labels': labels,
                  'advantage': advantage,
                  'description': description,
                  'address': address,
                  'publisher': publisher,
                  'hr_position': hr_position,
                  'aspiration': aspiration,
                  'domain': domain,
                  'phase': phase,
                  'scale': scale,
                  'home_page': home_page, }

    if len(company_re) == 11:
        investment = company_re[5].text.strip().split('\n')[0]
        lagou_dict['investment'] = investment


if __name__ == '__main__':
    content_parse(browser.page_source)
