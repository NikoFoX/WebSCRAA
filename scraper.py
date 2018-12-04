import bs4 as bs
import requests
import lxml

url = "https://en.wikipedia.org/wiki/Regression_testing"

soup = bs.BeautifulSoup("", "lxml")

def getSourceCode(url, package="bs"):
    if package == "bs":
        global soup
        data = requests.get(url)
        soup = bs.BeautifulSoup(data.content, 'lxml')
        return soup.prettify()
    elif package == "lxml":
        data = requests.get(url)
        data = data.content
        html = lxml.etree.HTML(data)
        parsed = lxml.etree.tostring(html, pretty_print=True, method="html")
        return parsed
        
    
print(getSourceCode(url, "lxml"))
#parsed = soup.findAll("div")
#print(parsed)


