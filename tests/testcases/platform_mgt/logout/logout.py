# -*- coding: utf-8 -*-
# @Time: 2022/11/22 15:53
# @Author: Leona
# @File: logout.py


# import requests
# import json
# from lib.my_unit import MyUnit
# from lib.generateTestCases import __generateTestCases
# from lib.log import logger
# from conf.url_configs import logoutUrl
#
#
# """
# 平台管理》退出登录
# """
#
#
# class Logout(MyUnit):
#     """平台管理》退出登录"""
#
#     def getTest(self, tx):
#         logger.info("****************退出登录接口开始****************")
#
#         caseNum = tx['test_num']
#         caseName = tx['test_name']
#         code = tx['code']
#         flag = tx['flag']
#         logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
#         reqParam = json.JSONDecoder().decode(tx['params'])
#         logger.info("*******测试数据： " + str(reqParam))
#         res = requests.get(url=logoutUrl, headers=self.headers).json()
#         logger.info("*******返回数据： " + str(res))
#         self.assertEqual(res['code'], code)
#         logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
#         logger.info("****************退出登录接口结束****************")
#
#     @staticmethod
#     def getTestFunc(arg1):
#         def func(self):
#             self.getTest(arg1)
#         return func
#
#
# __generateTestCases(Logout, "platformMgtData.xlsx", "logout")
#
# if __name__ == '__main__':
#     MyUnit.main()
