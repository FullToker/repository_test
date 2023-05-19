from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

def getTitle(url):
    try:
        html= urlopen(url)
    except HTTPError as e:
        return None
        # print(e)
    try:
        bs0bj=BeautifulSoup(html.read())
        title=bs0bj.body.h1
    except AttributeError as a:
        return None
    return title

title=getTitle("https://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

    