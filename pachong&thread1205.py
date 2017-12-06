#--coding='utf-8'--


import requests
from bs4 import BeautifulSoup
import threading
import queue
import time




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
        # threadLock.acquire()
        process_data(self.threadname,self.queue)
        # threadLock.release()
        print("Thread {0} is done!".format(self.threadname),time.ctime(time.time()))
        time.sleep(1)

def process_data(threadname,queue):
    while not exitflag:
        threadLock.acquire()
        if not queue.empty():
            url = queue.get()
            crawl1 = Crawl()
            item = crawl1.parse(url)
            threadLock.release()
            print("------------------------------------------------------")
            for i in item:
                print(threadname, i)
        else:
            threadLock.release()


if __name__ == "__main__":
    exitflag = 0
    threadList = ["No.1", "No.2", "No.3"]
    threadLock = threading.Lock()

    urlList = ['https://www.qidian.com/kehuan','https://www.qidian.com/lishi',
               'https://www.qidian.com/junshi','https://www.qidian.com/wuxia','https://www.qidian.com/youxi']
    threads = []
    parseQueue = queue.Queue(6)

    # 填充队列
    threadLock.acquire()
    for url in urlList:
        parseQueue.put(url)
    threadLock.release()

    # 创建新线程
    for name in threadList:
        thread = mythread(name, parseQueue)
        thread.start()
        threads.append(thread)

    # 等待队列清空
    while not parseQueue.empty():
        pass

    # 通知线程退出
    exitflag = 1

    for th in threads:
        th.join()

