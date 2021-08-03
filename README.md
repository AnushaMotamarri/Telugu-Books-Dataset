# Telugu-Books-Dataset
This project scrapes text from Telugu novels available at this [website](http://www.teluguone.com/grandalayam/books/novels)
## Dataset
Complete dataset can be downloaded from [here](https://drive.google.com/open?id=1MDiP-_S2RtAN7c9TLnKi8I2pxIgONIP0)

---
**(OR)**
If you choose to create dataset by yourself using the code, here you go.
## Requirements
* Python3
* Pip3 
* Telugu Language should be enabled in Language settings of your machine, to be able to see telugu text.
## Execution Steps
Open the terminal and change current working directory to the location into which you want to clone the project.
```
git clone https://github.com/AnushaMotamarri/Telugu-Books-Dataset
cd Telugu-Books-Dataset
pip3 install bs4
pip3 install requests
python3 extract_booklinks.py
python3 extract_linksofpages.py
python3 scrapebook.py
```
You should now be seeing utf8 files getting created in the `book_data` directory. Each utf8 file corresponds to single page of a book.

This Scraper is `website specific`. So, it does not work with other websites.

## Related works
A similar work on Telugu Newspaper dataset can be found [here](https://github.com/AnushaMotamarri/Telugu-Newspaper-Article-Dataset)
