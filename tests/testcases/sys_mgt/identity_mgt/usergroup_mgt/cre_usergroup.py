# -*- coding: utf-8 -*-
# @Time: 2022/11/7 15:01
# @Author: Leona
# @File: cre_usergroup.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userGroupMgtUrl
from lib.commonSQL import get_latest_group


"""
管理视图》系统设置》身份管理》用户组》新建用户组
"""


class CreUserGroup(MyUnit):
    """管理视图》系统设置》身份管理》用户组》新建用户组"""

    def getTest(self, tx):
        logger.info("****************创建用户组接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['name'] = reqParam['name'] + str(random.randint(10, 99))
        if flag ==2:
            latestUserGroup = get_latest_group()
            reqParam['name'] = latestUserGroup['name']
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=userGroupMgtUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建用户组接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreUserGroup, "creUserGroup", "userGroupMgtData.xlsx", "creUserGroup")

if __name__ == '__main__':
    MyUnit.main()