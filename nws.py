import bs4
import ttsp
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def news():
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    ns=[]
    for news in news_list:
        ns.append(news.title.text[0:news.title.text.find('-')])
    return ns

    
