# -*- coding: utf-8 -*-
# @Time: 2022/11/4 11:09
# @Author: Leona
# @File: edit_user.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from faker import Faker
from lib.log import logger
from conf.url_configs import userMgtUrl
from lib.commonSQL import get_latest_user


"""
管理视图》系统设置》身份管理》用户》编辑用户
"""


class EditUser(MyUnit):
    """管理视图》系统设置》身份管理》用户》编辑用户"""

    global userName
    userName = get_latest_user()['username']

    def getTest(self, tx):
        logger.info("****************编辑用户接口开始****************")
        latestUser = get_latest_user()
        caseNum = tx['test_num']
        code = tx['code']
        caseName = tx['test_name']
        flag = tx['flag']
        faker = Faker(locale='zh_CN')       # 定义faker对象
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqUrl = userMgtUrl + '/' + str(latestUser['id'])
        reqParam['username'] = userName
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['realname'] = reqParam['realname']+'_update'
            reqParam['email'] = faker.free_email()
            reqParam['phone'] = faker.phone_number()
        if flag == 2:
            reqParam['email'] = faker.free_email()
            reqParam['phone'] = faker.phone_number()
        if flag == 3:
            reqParam['email'] = faker.free_email()
        if flag == 4:
            reqParam['phone'] = faker.phone_number()
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.put(url=reqUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")

        logger.info("****************编辑用户接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditUser,"userMgtData.xlsx", "editUser")

if __name__ == '__main__':
    MyUnit.main()
