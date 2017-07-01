
from bs4 import BeautifulSoup
from urllib2 import urlopen

URL = urlopen("http://www3.forbes.com/entrepreneurs/25-most-expensive-schools-worth-every-penny").read()
soup = BeautifulSoup(URL,'xml')

print(soup.text)
