import bs4
import requests
import sys
print('Googling...') # display text while downloading the Google page
print(sys.argv[1:])
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[0]))
print(res.content)

#Retrieve top search result links
soup=bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.select('div#main > div > div > div > a')
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    print("Hello")
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
