# -*- coding: utf-8 -*-
# @Time: 2022/11/8 15:42
# @Author: Leona
# @File: search_groupmember.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import addGroupMemberUrl
from lib.commonSQL import get_latest_group_member
from lib.commonPanaCloud import getDC

"""
管理视图》系统设置》身份管理》用户组》搜索用户组成员
"""


class SearchGroupMember(MyUnit):
    """管理视图》系统设置》身份管理》用户组》搜索用户组成员"""
    global regionInfo
    regionInfo = getDC()


    def getTest(self, tx):
        logger.info("****************查询用户组成员接口开始****************")
        self.headers['region'] = regionInfo[0]['name']
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            groupMemberInfo = get_latest_group_member()
            reqParam['group_id'] = str(groupMemberInfo['group_id'])
        logger.info("*******测试数据： " + str(reqParam))
        res = requests.get(url=addGroupMemberUrl, headers=self.headers, data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************查询用户组成员接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(SearchGroupMember, "userGroupMgtData.xlsx", "searchGroupMember")

if __name__ == '__main__':
    MyUnit.main()
