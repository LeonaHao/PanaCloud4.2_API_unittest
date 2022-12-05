# -*- coding: utf-8 -*-
# @Time: 2022/11/16 18:20
# @Author: Leona
# @File: get_mirror.py


import requests
import json
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import mirrorUrl


"""
业务视图》云中心》镜像》获取镜像列表
"""


class GetMirrorList(MyUnit):
    """业务视图》云中心》镜像》获取镜像列表"""

    def getTest(self, tx):
        logger.info("****************获取镜像列表接口开始****************")

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 0:
            self.headers['Authorization'] = ''
        res = requests.get(url=mirrorUrl, headers=self.headers,data=reqParam).json()
        logger.info("*******返回数据： " + str(res))
        self.assertEqual(res['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取镜像列表接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(GetMirrorList, "mirrorMgtData.xlsx", "getMirrorList")

if __name__ == '__main__':
    MyUnit.main()
