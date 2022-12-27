# -*- coding: utf-8 -*-
# @Time: 2022/12/27 16:25
# @Author: Leona
# @File: get_pooluser.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import busiPoolUserUrl
from lib.commonPanaCloud import getBusiPool


"""
管理视图》业务池》获取业务池成员列表
"""


class GetBusiPoolUser(MyUnit):
    """管理视图》业务池》获取业务池成员列表"""

    def getTest(self, tx):
        logger.info("****************获取业务池成员列表接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        #获取要编辑的业务池id
        poolData = getBusiPool()['data']
        poolIdList = []
        for item in poolData:
            if 'Auto' in item['name']:
                poolIdList.append(item['id'])
        poolId = poolIdList[0]
        reqUrl = busiPoolUserUrl + '/?page=1&size=10&pool_id=' + str(poolId)
        logger.info("*******测试地址： " + str(reqUrl))
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''

        res = requests.get(url=reqUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取业务池成员列表接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetBusiPoolUser, "busipoolMgtData.xlsx", "getBusiPoolUser")

if __name__ == '__main__':
    MyUnit.main()
