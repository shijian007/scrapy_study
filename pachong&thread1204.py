import re
import requests
from bs4 import BeautifulSoup
import threading
import queue
import time


exitflag = 0

class Crawl():
    def __init__(self):
        self.UA = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")

    def parse(self,url):
        items = []
        r = requests.get(url,headers = {"User-Agent":self.UA})
        html = r.content
        soup = BeautifulSoup(html,"html.parser")
        titles = soup.findAll("a", class_='name')
        for title in titles:
            items.append(title.string)
        return items


class mythread(threading.Thread):
    def __init__(self,threadname,queue):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.queue = queue

    def run(self):
        print("Thread {0} is running!".format(self.threadname))
        threadLock.acquire()
        crawl1 = Crawl()
        item = crawl1.parse(self.queue)
        print("77777777777777777")
        for i in item:
            print(self.threadname,i)
        threadLock.release()
        print("Thread {0} is done!".format(self.threadname))


threadList = ["科幻", "历史", "军事"]
threadLock = threading.Lock()

urlList = ['https://www.qidian.com/kehuan','https://www.qidian.com/lishi','https://www.qidian.com/junshi']
threads = []
parseQueue = queue.Queue(6)

threadLock.acquire()
for url in urlList:
    parseQueue.put(url)
threadLock.release()


exitflag = 1

for name in threadList:
    if not parseQueue.empty():
        thread = mythread(name,parseQueue.get())
        thread.start()
        threads.append(thread)

for th in threads:
    th.join()

