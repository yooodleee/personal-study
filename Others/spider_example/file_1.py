from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com')
bs=BeautifulSoup(html, 'html.parser')

imageLocation=bs.find('a', {'id':'logo'}).find('img')['src']    #a태그와 {'id':'logo'}-> 'img' 태그['src'] 인덱싱
urlretrieve(imageLocation, 'logo.jpg')