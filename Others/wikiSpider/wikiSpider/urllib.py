from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com')
bs=BeautifulSoup(html, 'html.parser')
imageLocation=bs.find('a',{'id':'logo'}).find('img')['src']
urlretrieve(imageLocation, 'logo.jpg')

'''
http://www.pythonscraping.com에서 로고를 내려받아, 스크립트를 실행할\
디렉터리에 logo.jpg라는 이름으로 저장한다.
이 코드는 내려받을 파일이 하나뿐이고, 파일 이름과 확장자를 어떻게 정할지 알고 있다면\
잘 동작한다.
하지만 파일 하나만 내려받고 일을 끝내는 스크레이퍼는 거의 없다.
'''