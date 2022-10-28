# -*- coding: utf-8 -*-
# @Time: 2022/10/24 11:08
# @Author: Leona
# @File: search_flavor.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import flavorMgtUrl


"""
管理视图》系统设置》规格管理》查询规格
"""


class SearchFlavor(MyUnit):
    """管理视图》系统设置》规格管理》查询规格"""

    def getTest(self, tx):
        logger.info("****************查询规格接口开始****************")
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 1:
            self.headers['Authorization'] = ''
        res = requests.get(url=flavorMgtUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************查询规格接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(SearchFlavor, "searchFlavor", "flavorMgtData.xlsx", "searchFlavor")

if __name__ == '__main__':
    MyUnit.main()
