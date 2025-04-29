import requests
import pymysql

# MySQL 연결 설정
conn = pymysql.connect(
    host="localhost",
    user="eddi",
    password="eddi@123",
    database="wanted",
    charset='utf8mb4'
)
cursor = conn.cursor()

def get_wanted_jobs(query="개발자", limit=10, offset=0):
    url = "https://www.wanted.co.kr/api/v4/jobs"
    params = {
        "query": query,
        "limit": limit,
        "offset": offset,
        "country": "kr",
        "tag_type_ids": "518",  # 개발직군
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"API 호출 실패: {response.status_code}")
        return []

def insert_into_mysql(job):
    sql = """
        INSERT INTO wanted_jobs (id, company_name, position, location, reward, job_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            company_name=VALUES(company_name),
            position=VALUES(position),
            location=VALUES(location),
            reward=VALUES(reward),
            job_url=VALUES(job_url)
    """
    values = (
        job['id'],
        job['company']['name'],
        job['position'],
        job.get('location', ''),
        job.get('reward', 0),
        f"https://www.wanted.co.kr/wd/{job['id']}"
    )
    cursor.execute(sql, values)
    conn.commit()

if __name__ == "__main__":
    jobs = get_wanted_jobs(query="프론트엔드", limit=20)
    for job in jobs:
        insert_into_mysql(job)
        print(f"Inserted: {job['position']} at {job['company']['name']}")
