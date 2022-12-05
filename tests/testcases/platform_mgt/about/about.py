# -*- coding: utf-8 -*-
# @Time: 2022/11/22 10:33
# @Author: Leona
# @File: about.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import aboutUrl


"""
平台管理》关于
"""


class GetAboutInfo(MyUnit):
    """平台管理》关于"""

    def getTest(self, tx):
        logger.info("****************获取关于接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.get(url=aboutUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        if flag == 1:
            self.assertEqual(res['data']['address'],"http://udsafe.com.cn")
            self.assertEqual(res['data']['product'],"智慧筋斗云")
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取关于接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetAboutInfo, "platformMgtData.xlsx", "getAboutInfo")

if __name__ == '__main__':
    MyUnit.main()
