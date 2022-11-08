# -*- coding: utf-8 -*-
# @Time: 2022/10/20 10:31
# @Author: Leona
# @File: my_unit.py

import unittest
import os
from conf.base_config import libPath
from lib.log import logger
from lib.handle_yaml import read_yaml

'''构建myunit，提炼通用内容'''

class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("****************开始接口类测试******************")
        cls.token = read_yaml('token.yaml')


    def setUp(self) -> None:
        logger.info("****************开始接口测试********************")
        self.headers = {'Content-Type': 'application/json',
                    'Authorization': self.token
                    }

    def tearDown(self) -> None:
        logger.info("****************结束接口测试********************")



    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("****************结束接口类测试******************")
