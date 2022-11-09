# -*- coding: utf-8 -*-
# @Time: 2022/10/31 10:54
# @Author: Leona
# @File: cre_busipool.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import busiPoolMgtUrl


"""
管理视图》业务池》新建业务池
"""


class CreBusiPool(MyUnit):
    """管理视图》业务池》新建业务池"""

    def getTest(self, tx):
        logger.info("****************创建业务池接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['name'] = reqParam['name'] + "_rand_" + str(random.randint(1,1000))
        logger.info("*******测试数据： " + str(reqParam))

        result = requests.post(url=busiPoolMgtUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建业务池接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreBusiPool, "busipoolMgtData.xlsx", "creBusiPool")

if __name__ == '__main__':
    MyUnit.main()
