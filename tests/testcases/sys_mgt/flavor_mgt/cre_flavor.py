# -*- coding: utf-8 -*-
# @Time: 2022/10/24 11:08
# @Author: Leona
# @File: cre_flavor.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from configs.url_configs import flavorMgtUrl
from lib.commonSQL import get_latest_flavor


"""
管理视图》系统设置》规格管理》新建规格
"""


class CreFlavor(MyUnit):
    """管理视图》系统设置》规格管理》新建规格"""

    def getTest(self, tx):
        logger.info("****************创建规格接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 1:
            self.headers['Authorization'] = ''
        if flag == 2:
            latestFlavor = get_latest_flavor()
            reqParam['name'] = latestFlavor['name']
        logger.info("*******测试数据： " + str(reqParam))

        r = requests.post(url=flavorMgtUrl, headers=self.headers, json=reqParam, verify=False)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建规格接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreFlavor, "creFlavor", "flavorMgtData.xlsx", "creFlavor")

if __name__ == '__main__':
    MyUnit.main()
