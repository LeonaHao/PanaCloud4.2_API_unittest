# -*- coding: utf-8 -*-
# @Time: 2022/10/28 15:48
# @Author: Leona
# @File: commonPanaCloud.py

from lib.handle_yaml import read_yaml
from conf.url_configs import flavorMgtUrl
import requests

token = read_yaml('token.yaml')


#获取最新一条规格信息
def getLatestFlavor():
    headers = {'Content-Type': 'application/json',
               'Authorization': token}
    res = requests.get(url=flavorMgtUrl,headers=headers).json()
    latestFlavor = res['data'][0]
    return latestFlavor


