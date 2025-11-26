from bs4 import BeautifulSoup

class LinkedInParser:
    def __init__(self,html):
        self.soup = BeautifulSoup(html,"html.parser")

    def title(self):
        return self.soup.title.string if self.soup.title else "No title"