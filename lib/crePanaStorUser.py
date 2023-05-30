# -*- coding: utf-8 -*-
# @Time: 2023/5/8 15:27
# @Author: Leona
# @File: crePanaStorUser.py
import requests
import json



def batchCreUsers(startNum, endNum):
    baseUrl= 'https://172.16.176.70/'
    creUserUrl = baseUrl + 'v1/account/users/'
    headers ={"Content-Type":"application/json"}

    for i in range(startNum,endNum):
        reqParam ={
            "name":"u" + str(startNum),
            "password":"11112222",
            "group":[]
        }

        print(reqParam)
        requests.packages.urllib3.disable_warnings()
        res=requests.post(url=creUserUrl,headers=headers,json=reqParam,verify=False).json()
        if res['code']==0:
            print("用户创建成功")
        else:
            print("用户创建成功")
        startNum = startNum + 1


batchCreUsers(1,3)
