# -*- coding: utf-8 -*-
# @Time: 2022/11/8 14:08
# @Author: Leona
# @File: search_usergroup.py


import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userGroupMgtUrl

"""
管理视图》系统设置》身份管理》用户组》搜索用户组
"""


class SearchUserGroup(MyUnit):
    """管理视图》系统设置》身份管理》用户组》搜索用户组"""

    def getTest(self, tx):
        logger.info("****************查询用户组接口开始****************")
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        searchFieldList = ['name', 'description']
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['search_field'] = random.choice(searchFieldList)
        logger.info("*******测试数据： " + str(reqParam))
        res = requests.get(url=userGroupMgtUrl, headers=self.headers, data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************查询用户组接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func


__generateTestCases(SearchUserGroup, "userGroupMgtData.xlsx", "searchUserGroup")

if __name__ == '__main__':
    MyUnit.main()
