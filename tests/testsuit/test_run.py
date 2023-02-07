# -*- coding: utf-8 -*-
# @Time: 2022/10/19 14:04
# @Author: Leona
# @File: test_run.py

import sys
import os
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
import unittest
import time
from conf.base_config import testCasePath,report_file
from lib import send_email
from lib import HTMLTestRunner3,HTMLTestRunnerCN,handle_yaml
from lib.login import login



'''将token写入到yaml文件'''
token = {"token":login("admin","P@ssw0rd")}
handle_yaml.write_yaml(token,'token.yaml')



"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（testcase*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
suite = unittest.defaultTestLoader.discover(testCasePath, pattern='*.py')
# suite = unittest.defaultTestLoader.discover(os.path.join(testCasePath,'sys_mgt'), pattern='*.py')


with open(report_file,'wb') as rf:
    runner = HTMLTestRunner3.HTMLTestRunner(stream=rf, title='【QA环境】筋斗云4.2接口测试报告', description='测试用例结果如下所示：')
    # runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=rf,title='【QA环境】接口测试报告',description='测试用例结果如下所示：')
    runner.run(suite)

time.sleep(5)
send_email.send_email("【QA环境】PanaCloud4.2_接口测试报告")

