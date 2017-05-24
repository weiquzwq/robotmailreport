#coding=utf-8
import sys
import time
import json
from email.mime.text import MIMEText
from email.header import Header
import smtplib

class Report:

    @staticmethod
    def sendReport(mail_body):
        """

        :rtype: object
        """
        sendtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        subject=u'Lunkr4Web自动化测试日常报告'+'('+sendtime+')'
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'ceshi@coremail.cn'#发件地址
        #msg['To'] = 'wqzhou@coremail.cn,kfhuang@coremail.cn,jianli@coremail.cn,mlma@coremail.cn,dbzhong@coremail.cn,yxzhan@coremail.cn,jlwu@coremail.cn,cgyu@coremail.cn,cyt@coremail.cn,lwr@coremail.cn,lzhong@coremail.cn'#收件人地址，多人以分号分隔
        msg['To'] = 'wqzhou@coremail.cn,kfhuang@coremail.cn,mlma@coremail.cn,bqiu@coremail.cn'#收件人地址，多人以分号分隔
        smtp = smtplib.SMTP('smtp.coremail.cn')
        #smtp.set_debuglevel(1)#debug模式日志
        smtp.login('ceshi@coremail.cn', 'coremail+2016')#登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
        smtp.quit()
        print('test report has send out!')
