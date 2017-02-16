import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here 111111111 fg fgggggggggggg gggggggggggggg ")
you = "alex3287@bk.ru"
me = "alex3287@list.ru"
msg['Subject'] = "An Email Alert"
msg['From'] = me
msg['To'] = you
smtp_server = 'smtp.mail.ru'
s = smtplib.SMTP(smtp_server)
#s.send_message(msg)
s.sendmail(me, [you], msg.as_string())
s.quit()