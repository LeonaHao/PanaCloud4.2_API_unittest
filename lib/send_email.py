# -*- coding: utf-8 -*-
# @Time: 2022/10/18 16:28
# @Author: Leona
# @File: send_email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #混合MIME格式，支持上传附件
from email.header import Header    #用于使用中文邮件主题
from configs.base_config import *
from lib.log import logger


def send_email(reportTitle):
    '''
    :param reportTitle: 邮件标题
    :return:
    '''

    #1. 编写邮件内容
    with open(report_file,encoding='utf-8') as f:  #打开html报告
        email_body = f.read()  #读取报告内容

    #2.组装Email头（发件人、收件人、主题）
    msg = MIMEMultipart()     #混合MIME格式
    msg.attach(MIMEText(email_body,'html','utf-8'))   #添加html格式的邮件正文

    # content = '自动化测试报告详情，请查收附件！'
    # msg.attach(MIMEText(content,'plain','utf-8'))   #添加文本格式的邮件正文

    msg['From'] = sender
    msg['to'] = receiver
    msg['Subject'] = Header(reportTitle,'utf-8')

    #3. 构造附件，传送当前目录下的html文件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition']='attachment;filename="{}"'.format(report_file)
    msg.attach(att)

    #4. 发送邮件
    try:
        smtp = smtplib.SMTP_SSL(server)   #连接邮件服务器
        smtp.login(emailusername,emailpassword)  #登录邮件服务器
        smtp.sendmail(sender,receiver,msg.as_string())  #发送邮件
        logger.info("邮件发送完成")
    except Exception as e:
        logger.error(str(e))
    finally:
        smtp.quit()

