# -*- coding: utf-8 -*-
# @Time: 2023/1/11 18:45
# @Author: Leona
# @File: identity.py

import requests
from conf.url_configs import userGroupMgtUrl,userMgtUrl,delUserUrl
from lib.handle_yaml import read_yaml
from lib.commonSQL import get_userIds,get_userGroupIds

#获取token
token = read_yaml('token.yaml')

#删除用户
def delUser():

    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}

        Uid = get_userIds()

        for id in Uid:
            reqParam ={"id":[id['id']]}
            delUres = requests.post(url=delUserUrl,headers=headers,json=reqParam).json()
            if delUres['code'] == 0:
                print('**************{}删除成功**************'.format(id))
            else:
                print('**************{}删除失败**************'.format(id))
    except Exception as e:
        print(e)

#删除用户组
def delUG():

    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}
        #获取用户组列表
        # UGres = requests.get(url=userGroupMgtUrl,headers =headers, data={},verify=False).json()
        # UGId = []
        # for item in UGres['data']:
        #     UGId.append(item['id'])

        UGId = get_userGroupIds()

        for idItem in UGId:
            delUGurl = userGroupMgtUrl + str(idItem['id']) + '/del/'
            delUGres = requests.delete(headers=headers,url=delUGurl).json()
            if delUGres['code'] ==0:
                print('**************{}删除成功**************'.format(id))
            else:
                print('**************{}删除失败**************'.format(id))
    except Exception as e:
        print(e)



delUser()
delUG()