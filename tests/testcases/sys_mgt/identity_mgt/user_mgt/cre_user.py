# -*- coding: utf-8 -*-
# @Time: 2022/11/1 16:37
# @Author: Leona
# @File: cre_user.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from faker import Faker
from lib.log import logger
from conf.url_configs import userMgtUrl
from lib.commonSQL import get_latest_user


"""
管理视图》系统设置》身份管理》用户》新建用户
"""


class CreUser(MyUnit):
    """管理视图》系统设置》身份管理》用户》新建用户"""

    def getTest(self, tx):
        logger.info("****************创建用户接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        faker = Faker(locale='zh_CN')       # 定义faker对象
        reqParam = json.JSONDecoder().decode(tx['params'])
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['username'] = 'User1-_-' + str(random.randint(1, 100000))
            reqParam['realname'] = faker.name()
            reqParam['email'] = reqParam['username'] + '@udsafe.com.cn'
            reqParam['phone'] = faker.phone_number()
            reqParam['state'] = random.choice(['0', '1'])
        if flag ==2:
            latestUser = get_latest_user()
            reqParam['username'] = latestUser['username']
        if flag == 3:
            reqParam['username'] = reqParam['username']  + str(random.randint(10,99))
        logger.info("*******测试数据： " + str(reqParam))
        result = requests.post(url=userMgtUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建用户接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreUser, "userMgtData.xlsx", "creUser")

if __name__ == '__main__':
    MyUnit.main()