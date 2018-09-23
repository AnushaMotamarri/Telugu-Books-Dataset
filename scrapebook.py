import requests
import os,sys
from bs4 import BeautifulSoup
def scrape():
    os.mkdir("book_data")
    for i in range(1,376):
        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                resp=requests.get(url)
                if resp.status_code==200:
                    soup=BeautifulSoup(resp.text,'html.parser')
                    filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                    f=open("book_data/"+filename,'a+',encoding='utf_8')
                    for paras in soup.findAll("p"):
                        f.write(str(paras.get_text()))
scrape()
