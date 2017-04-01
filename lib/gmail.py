import imaplib
import email
import re
from bs4 import BeautifulSoup

from config import SMTP_SERVER

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail(email_address, email_password, folder='inbox', extract_pattern='/(72 jam)/'):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(email_address, email_password)
        mail.select(folder)

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    body = clean_mail_body(msg)
                    filtered_body = filter_text(body, extract_pattern)
                    print filtered_body + "\n"

    except Exception, e:
        print str(e)

def clean_mail_body(text):
    input_html = str(text)
    soup = BeautifulSoup(input_html, "html.parser")
    output_text = soup.get_text()
    return output_text

def filter_text(text, pattern):
    try:
        p = re.compile(pattern)
        found = p.search(text).group(1)
    except AttributeError:
        found = ''

    return found