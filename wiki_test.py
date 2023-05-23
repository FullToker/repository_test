from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取内链
def getInternalLinks(bs0bj,includeUrl):
    internalLinks=[]
    for link in bs0bj.findall("a",href=re.compile("^(\|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取外链
def getExternalLinks(bs0bj,excludeUrl):
    externalLinks=[]
    for link in bs0bj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bs0bj=BeautifulSoup(html)
    externalLinks=getExternalLinks(bs0bj,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
