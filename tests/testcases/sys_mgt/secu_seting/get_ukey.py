# -*- coding: utf-8 -*-
# @Time: 2022/12/28 13:58
# @Author: Leona
# @File: get_ukey.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import ukeyUrl


"""
系统设置》安全设置》获取ukey
"""


class GetUkey(MyUnit):
    """系统设置》安全设置》获取ukey"""

    def getTest(self, tx):
        logger.info("****************获取ukey接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqUrl = ukeyUrl
        logger.info("*******测试地址： " + str(reqUrl))
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.get(url=reqUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取ukey接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetUkey, "sysMgtData.xlsx", "getUkey")

if __name__ == '__main__':
    MyUnit.main()
