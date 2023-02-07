# -*- coding: utf-8 -*-
# @Time: 2023/1/13 11:03
# @Author: Leona
# @File: storage_tool.py

import requests
from conf.url_configs import datadiskUrl
from lib.handle_yaml import read_yaml
from lib.commonSQL import get_userIds

#获取token
token = read_yaml('token.yaml')

#创建云硬盘
def creDisk(Num,ProjectId,NodeName):

    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}

        reqParam ={
                "name":"cd"+ str(Num),
                "disk_type":"filesystem",
                "description":"自动化创建的数据盘cd" + str(Num),
                "pool_id":"zfsPool",
                "size":"1",
                "share_vol":"unshare",
                "project_id":str(ProjectId),
                "target":str(NodeName)
            }

        creDiskRes = requests.post(url=datadiskUrl,headers=headers,json=reqParam,verify=False).json()
        if creDiskRes['code'] == 0:
            print('**************数据盘{}创建成功**************'.format('cd'+str(Num)))
        else:
            print('**************数据盘{}创建失败**************'.format('cd'+str(Num)))

    except Exception as e:
        print(e)


def batchCreDisk(Range, Num,ProjectId,NodeName):
    for i in range(Range):
        creDisk(Num,ProjectId,NodeName)
        Num = Num +1


#creDisk(Num,ProjectId,NodeName)
# creDisk('3','bfcd27d52a81418b8f46c6c59c0973f4','node-1-dc-16-1')
batchCreDisk(20,10,'bfcd27d52a81418b8f46c6c59c0973f4','node-1-dc-16-1')