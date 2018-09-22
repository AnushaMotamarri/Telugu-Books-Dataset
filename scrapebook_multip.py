import requests
import os,sys
from bs4 import BeautifulSoup
from multiprocessing import Process
#books_file=open("finished_books.txt",'a+')
#os.mkdir("book_data")
def scrape1():

    for i in range(1,34):
        #print("book"+str(i)+" started")
        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))

def scrape2():
    for i in range(54,125):
        #print(i)
        #print("book"+str(i)+" started")
        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))

def scrape3():

    for i in range(109,151):
        #print(i)
        #print("book"+str(i)+" started")
        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))

def scrape4():

    for i in range(164,212):

        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))

def scrape5():

    for i in range(219,265):

        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))

def scrape6():
    for i in range(274,306):
        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))


def scrape7():

    for i in range(328,361):

        n_url=-1
        for page in open("book"+str(i)+".txt",'r'):
            url=page.strip()
            if(url!=""):
                n_url+=1
                filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                if(os.path.isfile("book_data/"+filename)==False):
                    print(str(i)+"-->"+str(n_url))
                    resp=requests.get(url)
                    if resp.status_code==200:
                        soup=BeautifulSoup(resp.text,'html.parser')
                        #filename="00"+'0'*(3-len(str(i)))+str(i)+'0'*(3-len(str(n_url)))+str(n_url)+".utf8"
                        f=open("book_data/"+filename,'a+',encoding='utf_8')
                        for paras in soup.findAll("p"):
                            f.write(str(paras.get_text()))


def main():
    p1=Process(target=scrape1)
    p2=Process(target=scrape2)
    p3=Process(target=scrape3)
    p4=Process(target=scrape4)
    p5=Process(target=scrape5)
    p6=Process(target=scrape6)
    p7=Process(target=scrape7)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
if __name__=="__main__":
    main()
#scrape1()
