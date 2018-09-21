import requests
from bs4 import BeautifulSoup
import os
def scrape():
    for k in range(0,361,30):
        i=1
        print(k)
        prev=""
        url='http://www.teluguone.com/grandalayam/books/novels'+str(k)+'.html'
        resp=requests.get(url)
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'html.parser')
            for anchor in soup.findAll("a"):
                link=anchor.get("href")
                if 'novels/' in str(link):
                    if(link!=prev):
                        if(i>=3):
                            f1=open("booklinks.txt",'a+',encoding='utf-8')
                            f1.write(link+"\n")
                            print(str(i)+" "+link)
                            prev=link
                        i=i+1

scrape()
