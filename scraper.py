import bs4 as bs
import requests
import lxml
from lxml import html
import re
import cssselect

url = "https://en.wikipedia.org/wiki/Regression_testing"

soup = bs.BeautifulSoup("", "lxml")
bsOutput = str()
lxmlOutput = str()

def getSourceCode(url, package="bs"):
    if package == "bs":
        global soup
        global bsOutput
        data = requests.get(url)
        soup = bs.BeautifulSoup(data.content, 'lxml')
        bsOutput = soup
        return soup.prettify()
    elif package == "lxml":
        global lxmlOutput
        data = requests.get(url)
        data = data.content
        html = lxml.etree.HTML(data)
        lxmlOutput = lxml.etree.tostring(html, pretty_print=True, method="html")
        return lxmlOutput

def getResponse(url):
        data = requests.get(url)
        data = data.content
        html = lxml.etree.HTML(data)
        return html
        
#parsed = soup.findAll("div")
#print(parsed)

#print(getSourceCode("https://justjoin.it/poznan", "lxml"))
"""
data = requests.get(url)
data = data.content

toFind = re.compile(r'#main-page-portals')

html = lxml.html.HTMLParser(data)
print(html)
"""