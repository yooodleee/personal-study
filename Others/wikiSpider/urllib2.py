#http://www.pythonscraping.com에서 src 속성이 있는 태그에 연결된 내부 파일을 모두 다운받자.
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory='downloaded'
baseUrl='http://www.pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url='http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url=source
    elif source.startswith('www.'):
        url=source[4:]
        url='http://{}'.format(baseUrl, source)
    
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path=absoluteUrl.replace('www', '')
    path=path.replace(baseUrl, '')
    path=downloadDirectory+path
    directory=os.path.dirname(directory)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html=urlopen('http://www.pythonscraping.com')
bs=BeautifulSoup(html, 'html.parser')
downloadList=bs.findAll(src=True)

for download in downloadList:
    fileUrl=getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))