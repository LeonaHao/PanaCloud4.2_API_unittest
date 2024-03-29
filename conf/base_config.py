# -*- coding: utf-8 -*-
# @Time: 2022/10/18 13:56
# @Author: Leona
# @File: base_config.py


'''
配置项目相关路径、发送邮件、访问数据库功能
'''
import sys
import os
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
import pymysql
import time


"""项目路径"""
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""测试数据路径"""
dataPath = os.path.join(basedir, 'datafiles')
"""日志路径"""
logPath = os.path.join(basedir, 'logs')
"""lib路径"""
libPath = os.path.join(basedir, 'lib')
"""测试用例路径"""
testCasePath = os.path.join(basedir, 'tests','testcases')
"""报告文件路径"""
curTime = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
report_file = os.path.join(basedir, 'reports',curTime +"_report.html")

"""数据库配置"""
panacloud = dict(host='172.16.20.11', user='root', passwd='P@ssw0rd', port=3306,db='panacloud4', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
panastor = dict(host='172.16.20.11', user='root', passwd='Admin@9000', port=3306,db='panastor', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# panacloud = dict(host='172.16.20.1', user='root', passwd='P@ssw0rd', port=3306,db='panacloud4', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# panastor = dict(host='172.16.20.1', user='root', passwd='Admin@9000', port=3306,db='panastor', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

"""邮件配置"""
sender = 'qa_auto@udsafe.com.cn'      #发件人
receiver = 'lijj@udsafe.com.cn'  #收件人      #系统测试部： qa@udsafe.com.cn

server = 'smtp.mxhichina.com'   #邮件服务器
emailusername = 'qa_auto@udsafe.com.cn'   #邮箱账号
emailpassword = 'Udsafe888'  #登陆邮箱的授权码，是授权码，不是邮箱密码

