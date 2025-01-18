import pymysql.connections

#연결 객체(conn)
#데이터베이스에 연결하고 정보를 보냄, 롤백(쿼리를 취소하고 데이터베이스를 이전 상태로 복귀시킴), 새 커서 객체를 만듬
#연결 객체 하나에 다수의 커서 객체-> 데이터베이스가 여러 개고 이들 전체에 정보를 저장할 때
conn=pymysql.connections(host='127.0.0.1', user='root', passwd='None', id='mysql')

#커서 객체(cur)-> 마지막에 실행한 쿼리 결과도 가지고 있음.
cur=conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id=1")
print(cur.fetchone())   #fetchone(): 커서에서 함수를 호출하여 이 정보에 접근

cur.close() #연결/커서 객체는 항상 닫아줘야 함(연결 누수 방지)
conn.close()

'''
연결 누수: 더는 사용하지 않는 연결인데도 소프트웨어 입장에서\
닫아도 된다는 확신이 없어서 닫히지 않은 연결이 쌓이는 현상

연결 누수가 심해지면 데이터베이스가 다운될 수 있음
'''

