import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def get_html(url):
    try:
         html = urllib.request.urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
    except AttributeError as e:
        return None
    return bsObj

obj = get_html('https://www.nytimes.com/')

print("Done")