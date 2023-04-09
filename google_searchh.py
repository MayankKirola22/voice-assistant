import requests, lxml
from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser
from serpapi import GoogleSearch

def searcher(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
def openner(query):
    for url in search(query, num_results=1):
        webbrowser.open(url)
        break
def quickbox(query):
    pass

#quickbox()
