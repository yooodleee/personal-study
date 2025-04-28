import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook
# from google.colab import drive
# drive.mount('/content/drive', force_remount=True)

POSTING_NUM_LIST = []
JOB_DESC_LIST = []          # 공고내용 (col-md-12)
TITLE_LIST = []             # 채용 공고 제목 (tm-mgt-title)
COMPANY_NAME_LIST = []      # 회사이름 (tm_h2_title_company_info)
CATEGORY_LIST = []          # 부분 (rc_categories_name)
URL_LIST = []

# (1001 ~ 47764) 천에서 4.7 만 (거의 5만 개)
# 시작: 1001
# 끝: 47682

def MAKE_URL():
    for i in range(1001, 47682, 1):
        URL = "https://www.wanted.co.kr/wd/" + str(i)
        URL_LIST.append(URL)

# MAIN
MAKE_URL()

ABC = ["A1", "B1", "C1", "D1"]
columns = [
    "회사이름",
    "직무",
    "유사직무",
    "채용내용"
]

write_wb = Workbook()
write_ws = write_wb.active

# Head Columns 만들기
for (alphabet, col) in zip(ABC, columns):
    write_ws[alphabet] = col

for i, URL in enumerate(URL_LIST):
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    soup = str(soup)

    jikmoo = soup[soup.find('"position":"') + 12 : soup.find('"reward":') - 2]
    # print("직무: ", jikmoo)
    yusa_jikmoo = soup[soup.find('"sub_categoryies":') + 18 : soup.find('"position":"') - 2]
    # print("유사직무: ", yusa_jikmoo)
    job_naeyoung = soup[soup.find('"jd":') + 5 : soup.find('"company_name":"') - 2]
    # print("채용 내용: ", job_naeyoung)
    company_name = soup[soup.find('"company_name":"') + 16 : soup.find('"lang":"') - 2]
    # print("회사이름: ", comapny_name)

    write_ws.append(
        [
            company_name,
            jikmoo,
            yusa_jikmoo,
            job_naeyoung
        ]
    )

write_wb.save("Wanted.csv") # save csv