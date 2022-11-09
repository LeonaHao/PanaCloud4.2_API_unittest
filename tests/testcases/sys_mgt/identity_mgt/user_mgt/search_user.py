# -*- coding: utf-8 -*-
# @Time: 2022/11/7 14:30
# @Author: Leona
# @File: search_user.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userMgtUrl


"""
管理视图》系统设置》身份管理》用户》搜索用户
"""


class SearchUser(MyUnit):
    """管理视图》系统设置》身份管理》用户》搜索用户"""

    

    def getTest(self, tx):
        logger.info("****************查询用户接口开始****************")
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        searchFieldList = ['username', 'realname', 'phone', 'email', 'state', 'description']
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['search_field'] = random.choice(searchFieldList)
        logger.info("*******测试数据： " + str(reqParam))
        res = requests.get(url=userMgtUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************查询用户接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(SearchUser, "userMgtData.xlsx", "searchUser")

if __name__ == '__main__':
    MyUnit.main()
