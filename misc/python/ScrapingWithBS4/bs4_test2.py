from bs4 import BeautifulSoup
import requests
import smtplib
import urllib2
from lxml import etree
url = 'https://www.xhibition.co/sitemap_products_1.xml?from=4603663748&to=8416225169'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
#proxies = {'https': '209.212.253.44'}
#req = urllib2.Request(url, headers=hdr, proxies=proxies)
req = urllib2.Request(url, headers=hdr)
#try:
#    page = urllib2.urlopen(req)
#except urllib2.HTTPError as e:
#    print(e.fp.read())
#content = page.read()
with open("sitemap") as fp:
  content=fp.read()

def parse(self, response):
    try:
        print(response.status)
        print('???????????????????????????????????')
        if response.status == 200:
            self.driver.implicitly_wait(5)
            self.driver.get(response.url)
            print(response.url)
            print('!!!!!!!!!!!!!!!!!!!!')

            # DO STUFF
    except httplib.BadStatusLine:
        pass
while True:
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all('loc')
    for link in links:
        if 'seeulater' and 'consortium' in link.text:
            print(link.text)
            jake = link.text

    print "*"*30
