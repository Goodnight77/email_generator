from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

    # Global variables 
file_path="C:\\Users\\MSI\\Desktop\\PROJECTS\\send_email"
extends="\\"

email="mohammedarbinsibi@gmail.com"
password="20488847"
to_add="mohammedarbi.nsibi@supcom.tn"


    # Send emails
def send_mail(filename,attachment,to_add):
    global email, password 
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = to_add
    msg["Subject"] = "test_mail"
    
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email,password)
    s.sendmail(email,to_add,msg.as_string())
    s.quit()

send_mail("test.txt","test.txt",to_add)
smtp.gmail.com