#파이썬의 scv 라이브러리를 사용하면 scv 파일을 쉽게 수정하거나 만들 수 있다.
import csv

csvFile=open('test.csv', 'w+')
try:
    writer=csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()