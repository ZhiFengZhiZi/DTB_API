# -*- encoding: utf-8 -*-

# 导入smtplib和MIMEText
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.utils import formataddr

class Email_class(object):

    def __init__(self,subject,touser):

        self.s = subject
        self.u = touser
        self.server = smtplib.SMTP('smtp.mxhichina.com', 25)

    def send_email(self):
        user = 'wangsiyuan@datoubao365.com'
        pwd = 'a83423745.'
        #to = ['******@139.com', '******@qq.com']
        msg = MIMEMultipart()
        msg['Subject'] = self.s
        msg['From'] = formataddr(["知风服务器系统监控",user])
        content1 = MIMEText('这里是正文！', 'plain', 'utf-8')
        msg.attach(content1)
        attfile = 'D:\\DTB_API\\report\\2017-10-31 15_57_53_result.html'
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