import requests
from bs4 import BeautifulSoup

class RequestHdr(object):
    def __init__(self, url):
        self.url = url

    def http_GET(self):
        res = requests.get(self.url)
        return res

    def http_POST(self, payload):
        res = request.post(self.url, payload);
        return res

class ContentPsr(RequestHdr):
    def __init__(self, url):
        if url == '':
            print 'Please input url'
            return

        super(ContentPsr, self).__init__(url) #call parent's constructor

    def parseTag(self, tagName):
        source =  self.http_GET()
        soup = BeautifulSoup(source.text, 'lxml')
        return soup.select(tagName)




