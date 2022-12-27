# -*- coding: utf-8 -*-
# @Time: 2022/12/27 17:40
# @Author: Leona
# @File: edit_dc.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import dcURL
from lib.commonPanaCloud import getDC


"""
运维管理》区域》编辑区域
"""


class EditDC(MyUnit):
    """运维管理》区域》编辑区域"""

    def getTest(self, tx):
        logger.info("****************编辑区域接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")

        #获取区域数据
        dcInfo = getDC()
        reqUrl = dcURL + '/' + str(dcInfo[0]['id'])
        logger.info("*******测试地址： " + str(reqUrl))
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.put(url=reqUrl, headers=self.headers,json=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************编辑区域接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(EditDC, "devOpsMgtData.xlsx", "editDC")

if __name__ == '__main__':
    MyUnit.main()
