import pandas as pd
import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host='123.123.123.123', user='DB계정', password='비밀번호', db='excel'
)
curs = conn.cursor(pymysql.cursors.DictCursor)


# excel file load
frontend_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\frontend_interview_question.xlsx')
backend_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\backend_interview_question.xlsx')
app_web_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\app_web_interview_question.xlsx')
ai_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\ai_interview_question.xlsx')
embedded_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\embedded_interview_question.xlsx')
devops_question = pd.read_excel('C:\lecture\personal_study\personal-study\Others\PROJECT_STUDY\project\asset\devops_interview_question.xlsx')

# db truncate tables
sql_truncate = 'truncate table excel.interview_question'

curs.execute(sql_truncate)
conn.commit()

# data insert to db
sql_insert_1 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(frontend_question)):
    curs.execute(sql_insert_1, tuple(frontend_question.values[idx]))
conn.commit()

sql_insert_2 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(backend_question)):
    curs.execute(sql_insert_2, tuple(backend_question.values[idx]))
conn.commit()

sql_insert_3 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(app_web_question)):
    curs.execute(sql_insert_3, tuple(app_web_question.values[idx]))
conn.commit()

sql_insert_4 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(ai_question)):
    curs.execute(sql_insert_4, tuple(ai_question.values[idx]))
conn.commit()

sql_insert_5 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(embedded_question)):
    curs.execute(sql_insert_5, tuple(embedded_question.values[idx]))
conn.commit()

sql_insert_6 = 'insert into excel interview_question values(%s, %s, %s, %s)'
for idx in range(len(devops_question)):
    curs.execute(sql_insert_6, tuple(devops_question.values[idx]))
conn.commit()