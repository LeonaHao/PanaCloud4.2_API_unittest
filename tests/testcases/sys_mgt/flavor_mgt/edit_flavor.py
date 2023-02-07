# -*- coding: utf-8 -*-
# @Time: 2022/10/24 11:08
# @Author: Leona
# @File: edit_flavor.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import flavorMgtUrl
from lib.commonPanaCloud import getLatestFlavor
from lib.commonSQL import get_latest_sysFlavor,get_old_sysFlavor


"""
管理视图》系统设置》规格管理》编辑规格
"""


class EditFlavor(MyUnit):
    """管理视图》系统设置》规格管理》编辑规格"""

    def getTest(self, tx):
        logger.info("****************编辑规格接口开始****************")
        latestFlavor = getLatestFlavor()
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqUrl = flavorMgtUrl + '/' + str(latestFlavor['id'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['name'] = latestFlavor['name'] + "_update"
        if flag == 2:
            oldSysFlavor = get_old_sysFlavor()
            reqParam['name'] = oldSysFlavor['name']
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************编辑规格接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditFlavor, "flavorMgtData.xlsx", "editFlavor")

if __name__ == '__main__':
    MyUnit.main()
