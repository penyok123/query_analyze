import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if __name__ == '__main__':
    fromaddr = 'lixiaofang@igengmei.com'
    password = 'hTx9kAikArsSNsDr'
    toaddrs = "lixiaofang@igengmei.com"

    content = 'hello, this is email content.'
    textApart = MIMEText(content)

    imageFile = 'doctor.txt'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    pdfFile = 'doctor.txt'
    pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)

    zipFile = 'doctor.txt'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
    m.attach(pdfApart)
    m.attach(zipApart)
    m['Subject'] = 'title'

    try:
        server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error', e)
