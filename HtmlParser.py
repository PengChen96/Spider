
from bs4 import BeautifulSoup
# import re

class HtmlParser(object):

    def geturls(self,soup):
        new_urls = set()
        links = soup.find_all('a')
        # print(links)
        for link in links:
            try:
                new_url = link['href']
            except Exception as error:
                print("HtmlParser geturls:",error)
            new_urls.add(new_url)
        # print(new_urls)
        return new_urls

    def parser(self,html_data):
        if html_data is None:
            print("HtmlParser html_data is none")
            return
        soup = BeautifulSoup(html_data,'html.parser',from_encoding = 'utf-8')
        new_urls = self.geturls(soup)
        return new_urls