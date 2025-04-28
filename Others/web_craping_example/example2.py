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

# # 직무별 검색 키워드 매핑
# job_keywords = {
#     "backend": "백엔드",
#     "frontend": "프론트엔드",
#     "web_app": "웹앱",
#     "ai": "AI",
#     "embedded": "임베디드",
#     "devops": "DevOps",
# }
#
# # 크롤링한 데이터를 담을 리스트
# all_jobs = []
#
# # 검색 및 상세 정보 크롤링
# for job_type, keyword in job_keywords.items():
#     print(f"크롤링 시작: {keyword}")
#
#     # (1) 검색 결과 가져오가
#     search_url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
#     response = requests.get(search_url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # (2) 채용 공고 링크 수집
#     # 실제 사이트 HTML 구조
#     job_links = []
#     for a_tag in soup.find_all('a', class_="JobCard_className__xxx"):
#         link = a_tag['href']
#         if not link.startswith('http'):
#             link = "http://www.wanted.co.kr" + link
#         job_links.append(link)
#
#     # (3) 상세 페이지 크롤링
#     for link in job_links:
#         time.sleep(1)   # 서버 부하 방지
#         job_resp = requests.get(link)
#         job_soup = BeautifulSoup(job_resp.text, "html.parser")
#
#         # 주요 업무, 자격 요건 등 추출(예시, 실제 구조는 달라서 조정 필요)
#         try:
#             main_tasks = job_soup.find('div', class_='JobDescription_className__xxx').text.strip()
#             qualifications = job_soup.find('div', class_='JobQualification_className__xxx').text.strip()
#             preferred = job_soup.find('div', class_='JobPreferred_className__xxx').text.strip()
#             tech_stack = [span.text for span in job_soup.find_all('span', class_='TechStack_className__xxx')]
#             benefits = job_soup.find('div', class_='JobBenefits_className__xxx').text.strip()
#             hiring_process = job_soup.find('div', class_='JobHiringProcess_className__xxx').text.strip()
#
#             job_data = {
#                 "직무": job_type,
#                 "링크": link,
#                 "주요업무": main_tasks,
#                 "자격요건": qualifications,
#                 "우대사항": preferred,
#                 "기술스택": tech_stack,
#                 "혜택 및 복지": benefits,
#                 "채용전형": hiring_process,
#             }
#             all_jobs.append(job_data)
#         except Exception as e:
#             print(f"크롤링 실패: {link} / 에러: {e}")
#
#
# # 결과를 CSV로 저장
# import pandas as pd
# df = pd.DataFrame(all_jobs)
# df.to_csv("wanted_jobs.csv", index=False, encoding="utf-8-sig")