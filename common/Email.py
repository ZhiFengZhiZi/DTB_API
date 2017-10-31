# -*- encoding: utf-8 -*-

# 导入smtplib和MIMEText
import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.utils import formataddr

class Email_class(object):

    def __init__(self,subject,touser,reportname):

        self.s = subject
        self.u = touser
        self.server = smtplib.SMTP('smtp.mxhichina.com', 25)
        #self.filename = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'\\report'+reportname
        self.filename = reportname


    def send_email(self):
        user = 'tester@datoubao365.com'
        pwd = 'a83423745.'
        #to = ['******@139.com', '******@qq.com']
        msg = MIMEMultipart()
        msg['Subject'] = self.s
        msg['From'] = formataddr(["自动化测试报告",user])
        content1 = MIMEText('这里是正文！', 'plain', 'utf-8')
        msg.attach(content1)
        attfile = self.filename
        basename = os.path.basename(attfile)
        fp = open(attfile, 'rb')
        att = MIMEText(fp.read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
        encoders.encode_base64(att)
        msg.attach(att)
#-----------------------------------------------------------

        self.server.login(user, pwd)
        self.server.sendmail(user, self.u, msg.as_string())
        print('发送成功')
        self.server.close()

if __name__ == "__main__":
    e = Email_class(subject="我是主题",touser=["chenjian@datoubao365.com"])

    e.send_email()