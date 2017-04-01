import imaplib
import email

from config import SMTP_SERVER

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail(email_address, email_password, folder='inbox'):
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
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = msg['body']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    print email_body

    except Exception, e:
        print str(e)
