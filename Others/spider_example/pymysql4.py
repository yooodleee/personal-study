#원격 smtp 서버에 접속할 때 localhost를 원격 서버 주소로 바꾸면 된다.
import smtplib
from email.mime.text import MIMEText    #패키지: smtplib, email

#MIMEText 객체-> 저수준 MIME 프로토콜로 전송할 수 있는 빈 이메일 형식을 만든다.
#SMTP 연결은 마임 프로토콜 위에서 동작한다.-> 파이썬은 이 객체를 정확한 형식의 이메일로 바꾼다.
msg=MIMEText('The body of the email is here')

msg['Subject']='An Email Alert'
msg['From']='ryan@pythonscraping.com'
msg['To']='webmaster@pythonscraping.com'

s=smtplib.SMTP('localhost') #smtplib 패키지에는 서버로의 연결을 처리하는 정보가 있음
#이 연결은 사용을 마칠 때마다 끊어서 서버 연결이 너무 늘어나지 않게 해야한다.
s.send_message(msg)
s.quit()