import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook


class Content: 
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1')