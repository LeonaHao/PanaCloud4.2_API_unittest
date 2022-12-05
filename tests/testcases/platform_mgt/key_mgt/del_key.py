# -*- coding: utf-8 -*-
# @Time: 2022/11/22 15:32
# @Author: Leona
# @File: del_key.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import delKeyUrl
from lib.commonPanaCloud import getLatestKey

"""
平台管理》密钥管理》删除密钥
"""


class DelKey(MyUnit):
    """平台管理》密钥管理》删除密钥"""

    def getTest(self, tx):
        logger.info("****************删除密钥接口开始****************")
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            keyId = getLatestKey()
            reqParam['id'] = [keyId['id']]
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=delKeyUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************删除密钥接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(DelKey, "platformMgtData.xlsx", "delKey")

if __name__ == '__main__':
    MyUnit.main()
