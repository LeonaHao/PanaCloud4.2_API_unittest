# -*- coding: utf-8 -*-
# @Time: 2022/11/8 11:28
# @Author: Leona
# @File: del_usergroup.py

import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userGroupMgtUrl,addGroupMemberUrl
from lib.commonSQL import get_latest_user,get_latest_group


"""
管理视图》系统设置》身份管理》用户组组》删除用户组组
"""


class DelUserGroup(MyUnit):
    """管理视图》系统设置》身份管理》用户组组》删除用户组组"""

    def getTest(self, tx):
        logger.info("****************删除用户组接口开始****************")
        latestUserGroup = get_latest_group()
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqUrl = userGroupMgtUrl + str(latestUserGroup['id']) + '/del/'
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqUrl = userGroupMgtUrl +  '9999999/del/'
        if flag == 2:
            userInfo = get_latest_user()
            addMemberParam = {"user_id":[userInfo['id']],"group_id":str(latestUserGroup['id'])}
            addMemberRes = requests.post(url=addGroupMemberUrl,headers=self.headers,json= addMemberParam,verify=False).json()
            if addMemberRes['code'] == 0:
                reqUrl = userGroupMgtUrl + str(latestUserGroup['id']) + '/del/'
            else:
                print("*******添加成员失败*******")

        logger.info("*******测试数据： " + str(reqParam))
        result = requests.delete(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************删除用户组接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(DelUserGroup, "userGroupMgtData.xlsx", "delUserGroup")

if __name__ == '__main__':
    MyUnit.main()