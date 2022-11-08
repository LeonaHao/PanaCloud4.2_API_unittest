# -*- coding: utf-8 -*-
# @Time: 2022/10/31 14:29
# @Author: Leona
# @File: get_busipool.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import busiPoolMgtUrl


"""
管理视图》业务池》获取业务池
"""


class GetBusiPool(MyUnit):
    """管理视图》业务池》获取业务池"""

    def getTest(self, tx):
        logger.info("****************获取业务池接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.get(url=busiPoolMgtUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取业务池接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetBusiPool, "getBusiPool", "busipoolMgtData.xlsx", "getBusiPool")

if __name__ == '__main__':
    MyUnit.main()
