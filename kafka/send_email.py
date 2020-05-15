import datetime
import traceback
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

begin = time.time()
print(begin)
my_sender = 'lixiaofang@igengmei.com'
my_pass = 'Wd3W9j5XDbcKQHiz'
my_user6 = "lixiaofang@igengmei.com"


def send_email_tome(stat_data):
    try:
        msg = MIMEText(stat_data, 'plain', 'utf-8')
        msg['From'] = formataddr(["李小芳", my_sender])
        msg["To"] = formataddr(["李小芳", my_user6])
        msg['Subject'] = str(datetime.date.today()) + "马甲超过次数啦，赶紧看一下"
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(my_sender, my_pass)
        print(time.time())
        server.sendmail(my_sender, [my_user6], msg.as_string())
        server.quit()
        print(time.time())
    except Exception:
        logging.error("catch exception,main:%s" % traceback.format_exc())


send_email_tome("1234555")
print(time.time() - begin)


# def mail(my_sender, my_pass, recipients):
#     try:
#         msg = MIMEText('这是一条测试邮件,请忽略', 'plain', 'utf-8')
#         msg['From'] = formataddr([" ", my_sender])
#         msg['To'] = formataddr([" ", recipients])
#         msg['Subject'] = "邮件测试"
#         server = smtplib.SMTP_SSL("smtp.qq.com", port=465)
#         server.login(my_sender, my_pass)
#         server.sendmail(my_sender, recipients, msg.as_string())
#
#         server.quit()  # 关闭连接
#         print("邮件发送成功")
#     except Exception as e:
#         print("邮件发送失败: ", e)
#
#
# if __name__ == '__main__':
#     print(time.time())
#     begin = time.time()
#     mail(my_sender, my_pass, my_user6)
#     print(time.time() - begin)
