# -*- coding: utf-8 -*-
# @Time: 2022/10/28 11:08
# @Author: Leona
# @File: del_flavor.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import delFlavorUrl
from lib.commonPanaCloud import getLatestFlavor
from lib.commonSQL import get_latest_sysFlavor


"""
管理视图》系统设置》规格管理》删除规格
"""


class DelFlavor(MyUnit):
    """管理视图》系统设置》规格管理》删除规格"""

    def getTest(self, tx):
        logger.info("****************删除规格接口开始****************")
        latestFlavor = getLatestFlavor()
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['ids'] = [latestFlavor['id']]
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=delFlavorUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************删除规格接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(DelFlavor, "flavorMgtData.xlsx", "delFlavor")

if __name__ == '__main__':
    MyUnit.main()
