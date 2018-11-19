import bs4 as bs
import requests

url = "https://en.wikipedia.org/wiki/Regression_testing"

soup = bs.BeautifulSoup("", "lxml")

def getSourceCode(url):
    global soup
    data = requests.get(url)
    soup = bs.BeautifulSoup(data.content, 'lxml')
    return soup.prettify()
    
getSourceCode(url)
parsed = soup.findAll("div")
print(parsed)