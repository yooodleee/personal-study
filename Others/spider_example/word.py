from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

wordFile=urlopen('http://pythonscraping.com/pages/WwordDocument.docx').read()   #url에서 워드 문서 받음
wordFile=BytesIO(wordFile)  #Bytes-> 바이너리 파일 객체로 읽음
document=ZipFile(wordFile)  
#ZipFile-> 파이썬의 zipfile 라이브러리로 압축을 풀고(.docx는 모두 압축되어 있음)
xml_content=document.read('word/document.xml')  #압축이 풀린 파일인 xml을 읽는다.
print(xml_content.decode('utf-8'))

'''
원격 워드 문서를 바이너리 파일 객체로 읽는다.
'''