import pymysql
import pymysql.cursors


# MySQL 서버 연결
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='eddi',       # DB 아이디
    password='eddi@123',  # DB 비밀번호
    database='wanted',      # DB 이름
    charset='utf8mb4',      # 한글 지원
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 객체 생성
cursor = conn.cursor()


# 모든 직군 url을 삽입
def insertJobGroups(jobGroups):
    sql = "INSERT INTO jobgroup (jobGroup, url) VALUES (%s, %s)"
    data = [(job['jobGroup'], job['url']) for job in jobGroups]
    cursor.executemany(sql, data)


# 채용 정보 삽입
def insertRecruitInfoList(table, recruitInfos):
    try:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {table} (jobGroup, url) vALUES (%s, %s)"
            data = [(info['jobGroup'], info['url']) for info in recruitInfos]
            cursor.executemany(sql, data)
        conn.commit()
    finally:
        conn.close()

# 채용 상세 정보 삽입
def insertRecruitInfo(table, recruitInfo):
    try:
        with conn.cursor() as cursor:
            sql = f"""
                INSERT INTO {table} (
                    recruitInfoId, jobGroup, region, company,
                    mainTask, qualification, preference,
                    welfare, deadline, workArea, mainTaskNouns, qualificationNouns
                ) VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s, %s, %s
                )
            """

            cursor.execute(sql, (
                recruitInfo['recruitInfoId'],
                recruitInfo['jobGroup'],
                recruitInfo['region'],
                recruitInfo['company'],
                recruitInfo['mainTask'],
                recruitInfo['qualification'],
                recruitInfo['preference'],
                recruitInfo['welfare'],
                recruitInfo['deadline'],
                recruitInfo['workArea'],
                recruitInfo['mainTaskNouns'],
                recruitInfo['qualificationNouns']
            ))
        conn.commit()
    finally:
        conn.close()

# 데이터 삽입
# def insertDB(table, data):
#     """
#     table: 테이블명 (string)
#     data: dict 타입, ex) {"column1": value1, "column2": value2}
#     """
#     columns = ', '.join(data.keys())
#     placeholders = ', '.join(['%s'] * len(data))
#     sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
#     values = tuple(data.values())

#     try:
#         cursor.execute(sql, values)
#         conn.commit()
#     except Exception as e:
#         print(f"Insert Error: {e}")
#         conn.rollback()


# 데이터 읽기 
def readDB(table):
    """
    table: 테이블명 (string)
    반환: 리스트 안에 딕셔너리들
    """
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM `{table}`"    # table 이름은(backtick)로 감싸주는 게 안전합니다. 
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
    except Exception as e:
        print(f"DB read error: {e}")
        return []
    finally:
        conn.close()