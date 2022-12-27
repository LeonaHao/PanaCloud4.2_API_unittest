# -*- coding: utf-8 -*-
# @Time: 2022/12/27 16:38
# @Author: Leona
# @File: get_pooluser.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import busiPoolUserUrl,userMgtUrl
from lib.commonPanaCloud import getBusiPool,getUsers
from faker import Faker
import random


"""
管理视图》业务池》添加业务池成员
"""


class AddBusiPoolUser(MyUnit):
    """管理视图》业务池》添加业务池成员"""

    def getTest(self, tx):
        logger.info("****************获取业务池成员接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        #获取业务池id
        poolData = getBusiPool()['data']
        poolIdList = []
        for item in poolData:
            if 'Auto' in item['name']:
                poolIdList.append(item['id'])
        poolId = poolIdList[0]

        #查看是否有用户，没有用户的话，创建一个用户
        usersInfo = getUsers()
        if len(usersInfo) == 0:
            creUserParam = {
            "username":"testUser4BP_" + str(random.randint(1, 100000)),
            "realname": Faker.name(),
            "email":"testUser4BP@udsafe.com.cn",
            "phone":Faker.phone_number(),
            "description":"自动创建的业务池沉管"
        }
            creUserRes = requests.post(url=userMgtUrl, headers=self.headers, json=creUserParam, verify=False).json()
            if creUserRes['code'] == 0:
                user_id = creUserRes['data']['id']
        user_id = usersInfo[0]['id']

        reqUrl = busiPoolUserUrl + '/'
        logger.info("*******测试地址： " + str(reqUrl))
        reqParam = json.JSONDecoder().decode(tx['params'])

        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam[0]['pool_id'] = str(poolId)
            reqParam[0]['user_id'] = user_id
            if caseNum == '004':
                reqParam[0]['user_id'] = '99999999999'
        res = requests.post(url=reqUrl, headers=self.headers,json=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取业务池成员接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(AddBusiPoolUser, "busipoolMgtData.xlsx", "addBusiPoolUser")

if __name__ == '__main__':
    MyUnit.main()
