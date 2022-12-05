# -*- coding: utf-8 -*-
# @Time: 2022/11/22 14:56
# @Author: Leona
# @File: edit_key.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import keyUrl



"""
平台管理》密钥管理》编辑密钥
"""


class EditKey(MyUnit):
    """平台管理》密钥管理》编辑密钥"""

    def getTest(self, tx):
        logger.info("****************编辑密钥接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            #查询是否有密钥，如果无密钥测创建一个密钥
            keyListRes = requests.get(url=keyUrl, headers=self.headers).json()
            if len(keyListRes['data']) == 0:
                requests.post(url=keyUrl, headers=self.headers, json={}, verify=False).json()
                keyListRes = requests.get(url=keyUrl, headers=self.headers).json()
            reqParam['id'] = keyListRes['data'][0]['id']
        logger.info("*******测试数据： " + str(reqParam))
        editKeyRes = requests.put(url=keyUrl, headers=self.headers, json=reqParam).json()
        logger.info("*******返回数据： " + str(editKeyRes))
        self.assertEqual(editKeyRes['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************编辑密钥接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditKey, "platformMgtData.xlsx", "editKey")


if __name__ == '__main__':
    MyUnit.main()
