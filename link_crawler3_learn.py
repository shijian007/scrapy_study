#--coding='utf-8'--

import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com'
UA = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")
# url = 'http://www.pm25.com/{0}'.format(city1)
r = requests.get(url,headers = {"User-Agent":UA})
html = r.content
soup = BeautifulSoup(html,"html.parser")
city = soup.find("a")
print(city)
