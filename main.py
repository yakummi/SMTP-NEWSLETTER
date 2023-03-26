import smtplib
from config import settings

receiver_email = ''
table_url = 'https://docs.google.com/spreadsheets/d/1nMyNsyZGaR47zDkFR4XBF9qbXxvsFu5DpBCZc6-6KUA/edit?hl=ru#gid=0'


with smtplib.SMTP_SSL(settings['ssl'], settings['port']) as server:
    server.login(settings['sender_email'], settings['password'])
    server.sendmail(settings['sender_email'], receiver_email, settings['message'])
    server.close()

