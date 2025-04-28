import pymysql


# MySQL 서버 연결
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='eddi',       # DB 아이디
    password='eddi@123',  # DB 비밀번호
    database='wanted',      # DB 이름
    charset='utf8mb4',      # 한글 지원
)

# 커서 객체 생성
cursor = conn.cursor()

# 데이터 삽입
def insertDB(table, data):
    """
    table: 테이블명 (string)
    data: dict 타입, ex) {"column1": value1, "column2": value2}
    """
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    values = tuple(data.values())

    try:
        cursor.execute(sql, values)
        conn.commit()
    except Exception as e:
        print(f"Insert Error: {e}")
        conn.rollback()


# 데이터 읽기 
def readDB(table):
    """
    table: 테이블명 (string)
    반환: 리스트 안에 튜플들
    """
    sql = f"SELECT * FROM {table}"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results