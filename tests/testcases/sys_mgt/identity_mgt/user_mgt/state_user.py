# -*- coding: utf-8 -*-
# @Time: 2022/11/7 10:48
# @Author: Leona
# @File: state_user.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import userMgtUrl
from lib.MySQLHelper import MySQLHelper
import time



"""
管理视图》系统设置》身份管理》用户》禁用or激活用户
"""


class StateUser(MyUnit):
    """管理视图》系统设置》身份管理》用户》禁用or激活用户"""

    def getTest(self, tx):
        logger.info("****************禁用or激活用户接口开始****************")
        caseNum = tx['test_num']
        code = tx['code']
        caseName = tx['test_name']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        sql = 'select * from profile_user where is_delete=0 and state=0 order by created_at desc limit 1'
        latestUser = MySQLHelper("panacloud").get_one(sql,params={})
        userId = latestUser['id']
        reqUrl = userMgtUrl + '/' + str(userId) + '/state'
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqUrl = userMgtUrl + '/99999/state'
        if flag == 2:
            sql1 = 'select * from profile_user where is_delete=0 and state=0 order by created_at desc limit 1'
            latestUser1 = MySQLHelper("panacloud").get_one(sql1,params={})
            userId1 = latestUser1['id']
            reqUrl = userMgtUrl + '/' + str(userId1) + '/state'
        if flag == 3:
            sql2 = 'select * from profile_user where is_delete=0 and state=1 order by created_at desc limit 1'
            latestUser2 = MySQLHelper("panacloud").get_one(sql2,params={})
            userId2 = latestUser2['id']
            reqUrl = userMgtUrl + '/' + str(userId2) + '/state'
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************禁用or激活用户接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(StateUser, "stateUser", "userMgtData.xlsx", "stateUser")

if __name__ == '__main__':
    MyUnit.main()
