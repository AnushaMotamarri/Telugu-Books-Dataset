import requests
import os,sys
from bs4 import BeautifulSoup
def pages():
    i=1
    for book in open("booklinks.txt",'r',encoding="utf-8"):
        if(i>=1):
            file="book"+str(i)+".txt"
            print(i)
            f1=open(file,'w+',encoding="utf-8")
            resp=requests.get(book.strip())
            if resp.status_code==200:
                soup=BeautifulSoup(resp.text,'html.parser')
                select=soup.findAll("select")
                for option in select[0].findAll("option"):
                    link=option.get("value")
                    f1.write(link+"\n")

        i=i+1
pages()
