import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# 1. 웹에서 게시물을 접근하는 방법 구현
# 2. 게시물에서 데이터를 크롤링하는 방법 구현
# 웹 -> 게시물 -> 데이터 순으로 접근 

def crawl_id(limit=100,offset=0):
    url = 'http://www.wanted.jobs/api/v4/jobs?'

    params ={1656232918453:'',    #사용자번호?
    'country': 'all',
    'tag_type_ids': 873,    #직무 카테고리 고유 id
    'job_sort': 'job.latest_order',    #최신순 정렬
    'locations': all,
    'years': -1,    #경력 이상
    'years': -1,    #경력 이하    경력상관없이 검색하려면 -1
    'limit': limit,    #한 번에 조회 가능한 수 (최대100)
    'offset': offset}    #조회할 게시물의 첫 index        ex) limit=100 offset=10  => 10번게시물부터 110번게시물까지 크롤링

    #서버에 url과 쿼리로 요청
    r = requests.get(url,
                     params = params)
    #요청한 데이터 json포멧으로 변환
    r = r.json()
    #json포멧 데이터중 id컬럼만 추출
    id_list = [i['id'] for i in r['data']]
    return id_list

def return_id_list():
    '''
    0번째 게시물부터 100개씩 크롤링 while true
    오류발생! => ex) 총 게시물이 321개인데 300개 크롤링 후 다음100개를 크롤링하려했기때문
    따라서 재귀호출을 통해 크롤링 수를 100개씩 -> 오류발생! -> 10개씩 -> 오류발생! -> 1개씩 크롤링하는 함수구현
    만약 게시물이 321개라면 300개 크롤링 -> 20개 크롤링 - 1개 크롤링 return
    '''
    id_list=[]
    def crawl_all_id(limit=100,offset=0):
        try:
            while True:
                id_list.extend(crawl_id(limit,offset))
                offset+=limit

        except:
            if limit != 1:
                return crawl_all_id(limit/10,offset)
    crawl_all_id()
    return id_list


def crawl_job(id_list):
    df_list = []
    
    for id in id_list:
        url = f'https://www.wanted.jobs/api/v4/jobs/{id}?1656259528432'
        r = requests.get(url)
        r = r.json()['job']

        #1개의 게시물 크롤링할때마다 데이터프레임에 append 또는 concat하는것보다
        #list에 append하고 마지막에 한번에 concat하는게 속도가 더 빠르다고 함
        df_list.append(pd.json_normalize(r))
        
    df = pd.concat(df_list, ignore_index=True)
    #단일 게시물을 크롤링해서 concat하다보니 index가 모두 0이므로 reset_index
    return df


def engineering(df):
    drop_col = []
    df = df.drop(drop_col,axis=1)
    return df
start = time.time()

id_list = return_id_list()
end=time.time()
print(end-start)

df_job = crawl_job(id_list)
end=time.time()
print(end-start)