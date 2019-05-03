import comments
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def scrape(url, phrase):
    client = uReq(url)
    html = client.read()
    client.close()

    page_soup = soup(html, "html.parser")

    if(comments.find_comments(url, phrase)):
        title = (page_soup.find_all("h1", {"class":"watch-title-container"})[0].text).strip()

    return url,title


