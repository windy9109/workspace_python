from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://127.0.0.1:5000/list")  

soup = BeautifulSoup(html, "html.parser") 
trs = soup.find("table").find_all("tr")
for idx,tr in enumerate(trs):
    if idx > 0:
        tds = tr.find_all()
        print (tds[1].text,tds[3].text)

