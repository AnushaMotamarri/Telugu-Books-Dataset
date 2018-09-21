# Telugu-Books-Dataset
This project scrapes text from all the pages of each Telugu book available at this [website](http://www.teluguone.com/grandalayam/books/novels)
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
