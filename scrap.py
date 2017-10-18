# coding:utf-8

import urllib.request
import urllib.error
from bs4 import BeautifulSoup

interest_filter = ["north korea", "baseball", "basketball", "china"]

def get_html(url):
    try:
         html = urllib.request.urlopen(url)
         html.encoding = 'utf8'
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
    except AttributeError as e:
        return None
    return bsObj

#get html info
obj = get_html('https://www.nytimes.com/')

#judge if error ro not?
if obj == None:
    print("Error happen")
else:
    print("HTML found !")

#get html title
title = obj.head.title.get_text()
#print(title)

#Sub section 
sub_sec = obj.find("ul", {"class":"mini-navigation-menu"})
#print(set(sub_sec.get_text()))

story_lists = obj.find_all("h2", {"class":"story-heading"})
#story_link = story_list.("href")
#print(story_list)

for story in story_lists:
    try:
        story_title = story.find('a').get_text()
        for story_link in story.find_all('a', href=True):
            print(story_title)
            print(story_link['href'])
    except UnicodeEncodeError:
        pass
    except AttributeError:
        pass


"""
f = open('BBB.txt', 'w', encoding = 'UTF-8')

for name in story_list:
    f.write(name.get_text())
    f.write('\n')
f.close()
print("QQQ")
#title = get_title(obj)
#print(title)
"""