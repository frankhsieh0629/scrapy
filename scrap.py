import urllib.request
from bs4 import BeautifulSoup
html = urllib.request.urlopen('https://www.nytimes.com/')
bsObj = BeautifulSoup(html.read(), "lxml")
#print(html)

