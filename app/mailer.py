import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

EMAIL = os.environ.get('OMNINGSSIMULATOR_EMAIL')
PW = os.environ.get('OMNINGSSIMULATOR_EMAIL_PW')

def notify(job, user):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = user.email
    msg['Subject'] = 'Your job is done: {}'.format(job.name)

    body = 'Hi, the job you have submitted has just finished and is ready for download.'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PW)
    text = msg.as_string()
    server.sendmail(EMAIL, user.email, text)
    server.quit()