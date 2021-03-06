import re
import requests
from bs4 import BeautifulSoup

class Crawl():
    def __init__(self):
        # self.url = url
        self.UA = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")

    def parse(self,url):
        item = {}
        r = requests.get(url,headers = {"User-Agent":self.UA})
        html = r.content
        soup = BeautifulSoup(html,"html.parser")
        item['title'] = soup.findAll("a", class_='name')
        return item



if __name__=="__main__":
    url = 'https://www.qidian.com/kehuan'
    crawl = Crawl()
    item = crawl.parse(url)

    print(item)
