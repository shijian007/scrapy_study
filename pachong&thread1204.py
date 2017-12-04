import re
import requests
from bs4 import BeautifulSoup
import threading
import Queue
import time


exitflag = 0

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



class mythread():
    def __init__(self,threadname,queue,url):
        self.threadname = threadname
        self.queue = queue
        self.url = url

    def run(self):
        print("Thread ONE is running!")
        threadLock.acquire()
        crawl1 = Crawl()
        crawl1






threadList = ["Thread-1", "Thread-2", "Thread-3"]
threadLock = threading.Lock()

urlList = ['https://www.qidian.com/kehuan','https://www.qidian.com/lishi','https://www.qidian.com/junshi']
threads = []
parseQueue = Queue.Queue(6)

threadLock.acquire()
for url in urlList:
    parseQueue.put(url)
threadLock.release()

while not parseQueue.empty():
    pass

exitflag = 1

for name in threadList:
    thread = mythread(name,parseQueue)
    thread.start()
    threads.append()

for thread in threads:
    thread.join()


crawl1 = Crawl()
item = crawl1.parse(url[0])

print(item)