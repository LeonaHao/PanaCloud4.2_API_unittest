# -*- coding: utf-8 -*-
# @Time: 2022/10/18 14:32
# @Author: Leona
# @File: login.py

import requests
import urllib3
from conf import url_configs


#获取登录token
def login(account,pwd):
    '''
    :param account:登录用户名
    :param pwd:登录密码
    :return: token
    '''
    try:
        headers = {"Content-Type":"application/json"}
        reqUrl = url_configs.loginUrl
        reqParam = {
            "username":account,
            "password":pwd    #P@ssw0rd
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
        token = result['data']['token']
        Token = 'TOKEN ' + str(token)
        return Token
    except Exception as e:
        print(e)

