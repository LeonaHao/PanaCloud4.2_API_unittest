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

'''获取最新一条规格信息'''
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



'''删除业务池'''
def del_busi_pool(poolId):
    try:
        url = busiPoolMgtUrl + '/' + str(poolId)
        print(url)
        poolDelRes = requests.delete(url=url,headers=headers).json()
        if poolDelRes['code'] == 0:
            print("***************业务池删除成功***************")
        else:
            print("***************业务池删除失败,结果为{}***************".format(poolDelRes))
    except Exception as e:
        print(e)


'''获取某个业务池的安全组数据'''
def getSecurityGroup(poolId):
    try:
        securityGrpList = requests.get(url=securityGrpUrl + '?project_id=' + str(poolId),headers=headers).json()
        return securityGrpList['data']
    except Exception as e:
        print(e)



'''获取区域数据'''
def getDC():
    try:
        DCList = requests.get(url=dcURL ,headers=headers).json()
        return DCList['data']
    except Exception as e:
        print(e)



'''获取用户数据'''
def getUsers():
    try:
        userList = requests.get(url=userMgtUrl ,headers=headers).json()
        return userList['data']
    except Exception as e:
        print(e)


'''删除用户数据'''
def delUsers():
    try:
        userList = getUsers()
        for user in userList:
            reqParam = {"id":[user['id']]}
            delUserRes = requests.post(url=delUserUrl,headers=headers,json=reqParam).json()
            if delUserRes['code'] == 0:
                print("***********用户删除成功***********")
            else:
                print("***********用户{}删除失败,结果为{}***********".format(user['username'],delUserRes))
    except Exception as e:
        print(e)


'''获取用户组数据'''
def getUserGroup():
    try:
        userGroupList = requests.get(url=userGroupMgtUrl ,headers=headers).json()
        return userGroupList['data']
    except Exception as e:
        print(e)


'''删除用户组数据'''
def delUserGroup():
    try:
        userGroupList = getUserGroup()
        for ug in userGroupList:
            delUgUrl = userGroupMgtUrl + str(ug['id']) + '/del/'
            delUgRes = requests.delete(url=delUgUrl,headers=headers).json()
            if delUgRes['code'] == 0:
                print("***********用户组删除成功***********")
            else:
                print("***********用户组{}删除失败,结果为{}***********".format(ug['name'],delUgRes))
    except Exception as e:
        print(e)



'''获取最新一条秘钥信息'''
def getLatestKey():
    try:
        res = requests.get(url=keyUrl,headers=headers).json()
        latestKey = res['data'][0]
        return latestKey
    except Exception as e:
        print(e)


# getUserGroup()
# delUserGroup()
# delUsers()
# getBusiPool()