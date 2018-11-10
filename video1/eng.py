import bs4

res = open('403.html', 'rb')
soup = bs4.BeautifulSoup(res)
s = soup.find_all('p', class_='reader-word-layer').contents
print(soup)
