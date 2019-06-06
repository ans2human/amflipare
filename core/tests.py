from requests import get
from lxml.html import fromstring
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re

allinks = []
q = 'realme c3'
url = "https://www.google.com/search?q="
url_req = url + q
raw = get(url_req)
soup = BeautifulSoup(raw.content, 'html5lib')
links = soup.findAll("a")
for link in links:
    a = link['href']
    if a.startswith("/url?"):
        allinks.append(a)
# for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
#     a = re.split(":(?=http)",link["href"].replace("/url?q=",""))
# url = a[0]
sites = ['amazon.in', 'flipkart.com'] 
# print(allinks)
aallinks = [i for e in sites for i in allinks if e in i]
print(aallinks)