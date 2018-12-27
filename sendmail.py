#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
from email.mime.multipart import MIMEMultipart

try:
    from settings import (SENDER_EMAIL, SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, SENDER_NAME, SMTP_SSL_TYPE)
except ImportError as e:
    pass

def send_mail(recipient, subject, body, body_html, file, encoding='utf-8'):
    session = None
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = Header(u'"{0}" <{1}>'.format(SENDER_NAME, SENDER_EMAIL), encoding)
    msg['To'] = recipient
    msg['Date'] = formatdate()
    msg.attach(MIMEText(body, 'plain', encoding))
    msg.attach(MIMEText(body_html, 'html', encoding))
    if file != "":
        att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att["Content-Disposition"] = 'attachment; filename=' + file
        msg.attach(att)
    else:
        pass
    try:
        if SMTP_SSL_TYPE == 'SMTP_SSL':
            session = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        else:
            session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            if SMTP_SSL_TYPE == 'SMTP_TLS':
                session.ehlo()
                session.starttls()
                session.ehlo()
        session.login(SMTP_USERNAME, SMTP_PASSWORD)
        session.sendmail(SENDER_EMAIL, recipient, msg.as_string())
    except Exception as e:
        raise e
    finally:
        if session:
            session.quit()

