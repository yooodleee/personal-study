import os   # 각 파일이 저장될 디렉터리가 있는지 확인-> 없으면 만듦/파이썬과 운영체제 사이의 인터페이스
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDiretory='download'
baseUrl='http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):

    if source.startswith('http://www.'):    #source가 'http://www.로 시작한다면(source 11번째부터 출력)
        url=f'http://{source[11:]}'
    elif source.startswith('http://'):  #source가 'http://로 시작한다면(url을 source로 초기화)
        url=source
    elif source.startswith('www'):  #source가 'www'로 시작한다면(source 3번째까지 출력)
        url=source[:4]
        url=f'http://{source}'
    else:
        url=f'http://{baseUrl}.{source}' 
    
    if baseUrl not in url:  #baseUrl이 url에 없다면-> None 값 
        return None 
    return url  #url 

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):   #외부 링크는 내려받지 않음
    path=absoluteUrl.replace('www.', '')    #absoluteUrl에서 www->''
    path=path.replace(baseUrl, '')  #baseUrl-> ''
    path=downloadDirectory+path
    directory=os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

html=urlopen('http://www/pythonscraping.com')
bs=BeautifulSoup(html, 'html.parser')
downloadList=bs.find(src=True)  #src 속성이 있는 태그에 연결된 내부 파일을 모두 다운받음

for download in downloadList:
    fileUrl=getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDiretory))