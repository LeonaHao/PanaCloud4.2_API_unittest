# -*- coding: utf-8 -*-
# @Time: 2022/11/4 14:20
# @Author: Leona
# @File: reset_pwd.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from faker import Faker
from lib.log import logger
from conf.url_configs import userMgtUrl
from lib.commonSQL import get_latest_user


"""
管理视图》系统设置》身份管理》用户》重置用户密码
"""


class ResetPwd(MyUnit):
    """管理视图》系统设置》身份管理》用户》重置用户密码"""

    global userName
    userName = get_latest_user()['username']

    def getTest(self, tx):
        logger.info("****************重置用户密码接口开始****************")
        latestUser = get_latest_user()
        caseNum = tx['test_num']
        code = tx['code']
        caseName = tx['test_name']
        flag = tx['flag']
        faker = Faker(locale='zh_CN')       # 定义faker对象
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqUrl = userMgtUrl + '/' + str(latestUser['id']) + '/set_password/'
        if flag == 0:
            self.headers['Authorization'] = ''
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************重置用户密码接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(ResetPwd, "userMgtData.xlsx", "resetPwd")

if __name__ == '__main__':
    MyUnit.main()
