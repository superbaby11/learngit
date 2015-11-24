#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import time


def sendmail(SMTP_Server,Account,Password,SendTo,Content,attachment):

    #发信邮箱
    #mail_from = 'wangwh@nco-china.com.cn'
    #收件邮箱
    #mail_to = mailList
    msg = MIMEMultipart()
    #定义标题
    msg['Subject']=u"OMC自动化平台测试报告"
    #定义发件人、收件人名称
    msg['From']= Account
    msg['To'] = SendTo
    Receiver = SendTo.split(",")
    #定义发送时间
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    #定义正文
    f = open(Content, 'rb')
    mail_body = f.read()
    f.close()
    body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(body)
    #定义附件
    f = open(attachment, 'rb')
    mail_attachment = f.read()
    f.close()
    att1 = MIMEText(mail_attachment,"base64","utf-8")
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=report.html'
    msg.attach(att1)
    
    #连接SMTP服务器
    smtp = smtplib.SMTP()
    smtp.connect(SMTP_Server)
    #用户名密码
    smtp.login(Account,Password)
    smtp.sendmail(Account,Receiver,msg.as_string())
    smtp.quit()
    print'email has send out!'
if __name__ == "__main__":
    SMTP_Server = 'smtp.ym.163.com'
    Account = "wangwh@nco-china.com.cn"
    Password = "asdf@123"
    import sys
    Content = sys.argv[1]
    attachment = sys.argv[2]
    SendTo = sys.argv[3]
    sendmail(SMTP_Server,Account,Password,SendTo,Content,attachment)