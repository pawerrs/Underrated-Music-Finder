from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def scrape(current_url):
    client = uReq(current_url)
    html = client.read()
    client.close()

    page_soup = soup(html, "html.parser")

    return (page_soup.find_all("h1", {"class":"watch-title-container"})[0].text).strip()