import requests
import pymysql
from datetime import datetime

# ✅ 1. MySQL 연결 설정
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='eddi',
        password='eddi@123',
        database='wanted',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# ✅ 2. 테이블 생성
def create_table():
    conn = connect_db()
    with conn:
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS recruit_jobs (
                id INT PRIMARY KEY,
                company_name VARCHAR(255),
                position VARCHAR(255),
                location VARCHAR(255),
                reward INT,
                job_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(sql)
        conn.commit()

# ✅ 3. Wanted API 호출 및 데이터 수집
def fetch_wanted_jobs(query="개발자", limit=20):
    url = "https://www.wanted.co.kr/api/v4/jobs"
    params = {
        "query": query,
        "limit": limit,
        "country": "kr"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["data"]

# ✅ 4. MySQL에 데이터 삽입
def insert_job(job):
    conn = connect_db()
    with conn:
        with conn.cursor() as cursor:
            sql = """
            INSERT IGNORE INTO recruit_jobs (id, company_name, position, location, reward, job_url)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(sql, (
                job['id'],
                job['company']['name'],
                job.get('position', ''),
                job.get('location', '서울'),  # 기본값 처리
                job.get('reward', 0),
                f"https://www.wanted.co.kr/wd/{job['id']}"
            ))
        conn.commit()

# ✅ 5. 전체 파이프라인 실행 함수
def run_pipeline():
    create_table()
    jobs = fetch_wanted_jobs(query="개발자", limit=50)
    for job in jobs:
        insert_job(job)
    print(f"{len(jobs)}건의 채용공고를 수집 및 저장했습니다.")

# ✅ 메인 실행
if __name__ == "__main__":
    run_pipeline()
