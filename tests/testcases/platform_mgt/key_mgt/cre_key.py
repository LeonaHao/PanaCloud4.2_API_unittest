# -*- coding: utf-8 -*-
# @Time: 2022/11/22 10:51
# @Author: Leona
# @File: cre_key.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import keyUrl



"""
平台管理》密钥管理》创建密钥
"""


class CreKey(MyUnit):
    """平台管理》密钥管理》创建密钥"""

    def getTest(self, tx):
        logger.info("****************创建密钥接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=keyUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建密钥接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreKey, "platformMgtData.xlsx", "creKey")


if __name__ == '__main__':
    MyUnit.main()
