
import sqlite3
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

##############################
def db():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/database/company.db")
        db.execute("")
        db.row_factory = dict_factory # JSON objects
        return db
    except Exception as ex:
        print("db function has an errror")
        print(ex)
    finally:
        pass


def send_mail(to_email, from_email,email_subject, email_body):

    try:
        
        message = MIMEMultipart()
        message["To"] = to_email
        message["From"] = from_email
        message["Subject"] = email_subject




        messageText = MIMEText(email_body, 'html')
        message.attach(messageText)

        email = 'jachobwesth@gmail.com'
        password = 'xlcsplckzsaeinre'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo('Gmail')
        server.starttls()
        server.login(email,password)
        server.sendmail(from_email,to_email,message.as_string())
        server.quit()
    except Exception as ex:
        print(ex)
        return "error"