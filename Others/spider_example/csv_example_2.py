import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs=BeautifulSoup(html, 'html.parser')

#비교 테이블은 현재 페이지의 첫 번째 테이블.
table=bs.findAll('table', {'class': 'wikitalbe'})[0]
rows=table.findAll('tr')

csvFile=open('editors.csv', 'wt+')
writer=csv.writer(csvFile)

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writers(csvRow)
finally:
    csvFile.close()