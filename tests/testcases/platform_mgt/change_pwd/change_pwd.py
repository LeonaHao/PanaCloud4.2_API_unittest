# -*- coding: utf-8 -*-
# @Time: 2022/11/22 15:57
# @Author: Leona
# @File: change_pwd.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import setUserPwdUrl



"""
平台管理》密码管理》修改密码
"""


class ChangePwd(MyUnit):
    """平台管理》密码管理》修改密码"""

    def getTest(self, tx):
        logger.info("****************修改密码接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=setUserPwdUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************修改密码接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(ChangePwd, "platformMgtData.xlsx", "changePwd")


if __name__ == '__main__':
    MyUnit.main()
