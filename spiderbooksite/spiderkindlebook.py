from bs4 import BeautifulSoup as bs
import os
import sys
import urllib.request
from urllib.parse import quote
import string
import urllib
# coding=utf-8



def downloadByUrl(url):
    #html_data = urllib.request.urlopen(url).read().decode('utf-8')
#    url=urllib.parse.quote(url,safe=':/')
    print(url)
    html_data = urllib.request.urlopen(url).read()
    soup=bs(html_data,'html.parser')
    trcontent = soup.select("#jieguo tr")
    for content in trcontent:
        acontent = content.a
        if acontent == None:
            continue
        name = content.select("td:nth-of-type(1)")[0].string
        suffix = content.select("td:nth-of-type(2)")[0].string
        storageDir=sys.path[0]+'/books/'+key
        LocalPath = storageDir+"/books/"+name+"."+suffix
        bookurl =content.find("a")['href']
        if not os.path.exists(storageDir):
            os.makedirs(storageDir)
        if os.path.exists(LocalPath):
            print("the file is exists "+LocalPath)
            continue
        print("downloading file:"+name +" at path:"+LocalPath)
        try:
            bookurl=urllib.parse.quote(bookurl,safe=string.printable)
            urllib.request.urlretrieve(bookurl,LocalPath)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            continue
        print("downloadfile:"+name+"download end")

    nexttag=soup.find("a",text="下一页")
    if nexttag == None:
        print(key+" download end")
    else :
        nextlink=urllib.parse.quote(nexttag['href'].replace(' ', ''),safe=string.printable)
        print("next page url:"+nextlink)
        downloadByUrl(site+nextlink)


site = 'https://sk.kindleshare.cn/'
booksKwFile= open(sys.path[0]+"/bookskeyword","r+",encoding='utf-8')
for key in booksKwFile.readlines():
    key = key.strip('\n')
    print(key)
    keyword=quote(key)
    url= site +'?name='+keyword+'&submit=Search'
    downloadByUrl(url)