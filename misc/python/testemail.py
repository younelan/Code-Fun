#!/usr/bin/env python
#send html mail with smtplib
import smtplib
from email.mime.text import MIMEText

fp = open('testattach.txt', 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "bob@example.com" 
msg['To'] = "alice@example.com"
msg['Subject'] = 'Woohoo, testing mail'

s = smtplib.SMTP('localhost')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()

