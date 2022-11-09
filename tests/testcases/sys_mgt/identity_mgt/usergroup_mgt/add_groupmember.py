# -*- coding: utf-8 -*-
# @Time: 2022/11/8 14:29
# @Author: Leona
# @File: add_groupmember.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import addGroupMemberUrl
from lib.commonSQL import get_latest_group,get_latest_user


"""
管理视图》系统设置》身份管理》用户组》添加用户组成员
"""


class AddGroupMember(MyUnit):
    """管理视图》系统设置》身份管理》用户组》添加用户组成员"""

    def getTest(self, tx):
        logger.info("****************添加用户组成员接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        latestUserGroup = get_latest_group()
        reqParam['group_id'] = latestUserGroup['id']
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['group_id'] = 9999999
        if flag == 2:
            userInfo =get_latest_user()
            reqParam['user_id'] = [userInfo['id']]
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=addGroupMemberUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************添加用户组成员接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(AddGroupMember, "userGroupMgtData.xlsx", "addGroupMember")

if __name__ == '__main__':
    MyUnit.main()