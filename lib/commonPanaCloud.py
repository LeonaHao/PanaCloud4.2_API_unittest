# -*- coding: utf-8 -*-
# @Time: 2022/10/28 15:48
# @Author: Leona
# @File: commonPanaCloud.py

import requests
import json
from lib.handle_yaml import read_yaml
from conf.url_configs import *


token = read_yaml('token.yaml')
headers = {'Content-Type': 'application/json',
           'Authorization': token}

#获取最新一条规格信息
def getLatestFlavor():
    try:
        res = requests.get(url=flavorMgtUrl,headers=headers).json()
        latestFlavor = res['data'][0]
        return latestFlavor
    except Exception as e:
        print(e)


'''获取业务池列表'''
def getBusiPool():
    try:
        poolListRes = requests.get(url=busiPoolMgtUrl,headers=headers).json()
        return poolListRes
    except Exception as e:
        print(e)

#获取某个业务池的安全组数据
def getSecurityGroup(poolId):
    try:
        securityGrpList = requests.get(url=securityGrpUrl + '?project_id=' + str(poolId),headers=headers).json()
        return securityGrpList['data']
    except Exception as e:
        print(e)





