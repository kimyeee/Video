# import dramatiq
import requests


# @dramatiq.actor
def count_words(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")

    count_words('http://www.baidu.com')

res = requests.get('https://student.lxhelper.com/api/v1/')
print(res.text)