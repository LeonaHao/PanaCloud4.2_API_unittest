# -*- coding: utf-8 -*-
# @Time: 2022/12/28 14:30
# @Author: Leona
# @File: edit_key.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import ukeyUrl


"""
管理视图》系统设置》安全设置》编辑ukey
"""


class EditUkey(MyUnit):
    """管理视图》系统设置》安全设置》编辑ukey"""

    def getTest(self, tx):
        logger.info("****************编辑ukey接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqUrl = ukeyUrl 
        if flag == 0:
            self.headers['Authorization'] = ''

        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************编辑ukey接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditUkey, "flavorMgtData.xlsx", "EditUkey")

if __name__ == '__main__':
    MyUnit.main()
