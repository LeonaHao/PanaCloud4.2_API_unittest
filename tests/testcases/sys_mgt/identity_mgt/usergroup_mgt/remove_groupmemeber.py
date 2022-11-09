# -*- coding: utf-8 -*-
# @Time: 2022/11/8 14:43
# @Author: Leona
# @File: remove_groupmemeber.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import removeGroupMemberUrl
from lib.commonSQL import get_latest_group_member


"""
管理视图》系统设置》身份管理》用户组》移除用户组成员
"""


class RemoveGroupMember(MyUnit):
    """管理视图》系统设置》身份管理》用户组》移除用户组成员"""

    def getTest(self, tx):
        logger.info("****************移除用户组成员接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        latestGroupMember = get_latest_group_member()
        reqParam['group_id'] = latestGroupMember['group_id']
        reqParam['member_id'] = [latestGroupMember['id']]
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['member_id'] = [9999999]
        if flag == 2:
            reqParam['group_id'] = 9999999
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=removeGroupMemberUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************移除用户组成员接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(RemoveGroupMember, "userGroupMgtData.xlsx", "removeGroupMember")

if __name__ == '__main__':
    MyUnit.main()