# -*- coding: utf-8 -*-
# @Time: 2022/11/7 10:22
# @Author: Leona
# @File: del_user.py



import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import delUserUrl
from lib.commonSQL import get_latest_user


"""
管理视图》系统设置》身份管理》用户》删除用户
"""


class DelUser(MyUnit):
    """管理视图》系统设置》身份管理》用户》删除用户"""

    def getTest(self, tx):
        logger.info("****************删除用户接口开始****************")
        latestUser = get_latest_user()
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['id'] = [latestUser['id']]
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=delUserUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************删除用户接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(DelUser, "delUser", "userMgtData.xlsx", "delUser")

if __name__ == '__main__':
    MyUnit.main()
