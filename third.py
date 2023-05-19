from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re

def getHtml(url):
    try:
        html= urlopen(url)
    except HTTPError as e:
        return None
        # print(e)
    return html

url="http://en.wikipedia.org/wiki/Kevin_Bacon"
# url None异常处理
html=getHtml(url)
'''
if html==None:
    print("Error")
else:
    bs0bj=BeautifulSoup(html)
    # print(bs0bj.find("table",{"id":"giftList"}))
    try:
        #for child in bs0bj.find("table",{"id":"giftList"}).children:
            #print(child.get_text())

        print("tr:")
        print(bs0bj.find("table",{"id":"giftList"}).tr.get_text())
        for brother in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
            print(brother)
    except:
        print("Error2")
'''

bs0bj=BeautifulSoup(html)

for link in bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    # print(link)
    if 'href' in link.attrs:
        print(link.attrs['href'])
