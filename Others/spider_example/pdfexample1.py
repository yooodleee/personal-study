from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):   
    #urlopen에서 파이썬 파일 객체를 반환하지 않고 다음 행으로 대체하기만 하면 된다.
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr,device, pdfFile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return content

pdfFile=urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString=readPDF(pdfFile)
print(outputString)
pdfFile.close()