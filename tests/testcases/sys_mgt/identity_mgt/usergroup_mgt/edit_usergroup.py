# -*- coding: utf-8 -*-
# @Time: 2022/11/8 10:59
# @Author: Leona
# @File: edit_usergroup.py

import requests
import json,random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userGroupMgtUrl
from lib.commonSQL import get_latest_group
from lib.MySQLHelper import MySQLHelper


"""
管理视图》系统设置》身份管理》用户组组》编辑用户组组
"""


class EditUserGroup(MyUnit):
    """管理视图》系统设置》身份管理》用户组组》编辑用户组组"""

    global ugId
    ugId = get_latest_group()['id']

    def getTest(self, tx):
        logger.info("****************编辑用户组接口开始****************")
        latestUserGroup = get_latest_group()
        caseNum = tx['test_num']
        code = tx['code']
        caseName = tx['test_name']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqParam['id'] = ugId
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['name'] = reqParam['name'] + str(random.randint(10, 99))
        if flag == 2:
            sql = 'select * from profile_user_groups where is_delete=0 order by created_at asc limit 1;'
            param = ()
            earliestUG = MySQLHelper("panacloud").get_one(sql=sql,params=param)
            reqParam['name'] = earliestUG['name']
        if flag == 3:
            reqParam['id'] = '999999'
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=userGroupMgtUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************编辑用户组接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditUserGroup, "userGroupMgtData.xlsx", "editUserGroup")

if __name__ == '__main__':
    MyUnit.main()
