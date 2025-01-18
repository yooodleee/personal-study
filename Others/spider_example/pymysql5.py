import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg=MIMEText(body)
    msg['subject']=subject
    msg['From']='Christmas_alerts@pythonscraping.com'
    msg['To']='ryan@pythonscraping.com'

    s=smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bs=BeautifulSoup(urlopen('http://isischristmas.com/'))
while(bs.find('a', {'id':'answer'}).attrs['title']=='NO'):
    print('It is not Christmas yet.')
    time.sleep(3600)
    bs=BeautifulSoup(urlopen('http://isitchristmas.com/'))

sendMail('It is Christmas!',
         'According to http://itischristmas.com, it it christams!')
