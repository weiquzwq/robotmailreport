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
        subject=u'自动化测试日常报告'+'('+sendtime+')'
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'ceshi'#发件地址
        msg['To'] = 'wqzhou@'#收件人地址，多人以分号分隔
        smtp = smtplib.SMTP('smtp.163.cn')
        #smtp.set_debuglevel(1)#debug模式日志
        smtp.login('')#登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
        smtp.quit()
        print('test report has send out!')
