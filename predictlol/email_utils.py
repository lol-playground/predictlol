import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, os, glob
sys.path.append("../config")
import config

def email(to, subject, text):#, attach):
   msg = MIMEMultipart()

   msg['From'] = config.gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   # part = MIMEBase('application', 'octet-stream')
   # part.set_payload(open(attach, 'rb').read())
   # Encoders.encode_base64(part)
   # part.add_header('Content-Disposition',
   #         'attachment; filename="%s"' % os.path.basename(attach))
   # msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(config.gmail_user, config.gmail_pwd)
   mailServer.sendmail(config.gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()