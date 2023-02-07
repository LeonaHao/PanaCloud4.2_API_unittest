# -*- coding: utf-8 -*-
# @Time: 2022/12/28 11:08
# @Author: Leona
# @File: get_sysnet.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import sysNetUrl


"""
运维管理》基础网络》获取系统网络
"""


class GetSysnetList(MyUnit):
    """运维管理》基础网络》获取系统网络"""

    def getTest(self, tx):
        logger.info("****************获取系统网络接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqUrl = sysNetUrl + '?role=system'
        logger.info("*******测试地址： " + str(reqUrl))
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.get(url=reqUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取系统网络接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetSysnetList, "devOpsMgtData.xlsx", "getSysnet")

if __name__ == '__main__':
    MyUnit.main()
