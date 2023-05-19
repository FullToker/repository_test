from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re


'''
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj=BeautifulSoup(html)
namelist=bs0bj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_text())
namelist=bs0bj.findAll(text="the prince")
print(len(namelist))'''

def getHtml(url):
    try:
        html= urlopen(url)
    except HTTPError as e:
        return None
        # print(e)
    return html

url="http://www.pythonscraping.com/pages/page3.html"
html=getHtml(url)

# url None异常处理
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
parent1=bs0bj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling
print(parent1)
print(parent1.get_text().strip())
images=bs0bj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img[0-9]*\.jpg")})
for img in images:
    print(img.attrs)
    print(img["src"])

doubleTag=bs0bj.findAll(lambda tag: len(tag)==2)
for tag in doubleTag:
    print(doubleTag)
