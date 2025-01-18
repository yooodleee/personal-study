from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile=urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile=BytesIO(wordFile)
document=ZipFile(wordFile)
xml_content=document.read('word/document.xml')

wordObj=BeautifulSoup(xml_content.decode('utf-8'))
textStrings=wordObj.findAll('w:t')  
#<w:t></w:t> 태그를 기준으로 줄을 바꾸면 워드가 텍스트를 어떻게 나누는지 알기 쉽다.
for textElem in textStrings:
    closeTag=''
    try:
        style=textElem.previousSiblings.find('w:pstyle')
        if style is not None and style['w:val']=='Title':
            print('<h1>')
            closeTag='</h1>'
    except AttributeError:
        #출력할 태그가 없다.
        pass
    print(textElem.text)
    print(closeTag)