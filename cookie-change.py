#--coding=utf-8--
'''
scrapy 的cookie与直接从网上得到的cookie需要转化
'''

class cookieTrans():
    def __init__(self,cookie):
        self.cookie = cookie

    def cookiechange(self):
        itemDict = {}
        items = self.cookie.split(';')
        for i in items:
            key = i.split('=')[0].replace(' ','')
            value = i.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "网页F12-查看Network--查看Cookie--填在此处"
    Cookie = cookieTrans(cookie)
    print(Cookie.cookiechange())


