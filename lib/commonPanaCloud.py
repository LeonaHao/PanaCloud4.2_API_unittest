# -*- coding: utf-8 -*-
# @Time: 2022/10/28 15:48
# @Author: Leona
# @File: commonPanaCloud.py

import requests
import json
from lib.handle_yaml import read_yaml
from conf.url_configs import *
from faker import Faker
from lib.commonSQL import get_userIds,get_userGroupIds
import random


token = read_yaml('token.yaml')
headers = {'Content-Type': 'application/json',
           'Authorization': token}
# 定义faker对象
faker = Faker(locale='zh_CN')

#创建业务池参数配置
switch4PoolSecurity = ['true','false']   #设置业务池是否开启池安全
allowBlockList = ['allow','block']    #设置所有  禁用/允许  参数
privilegeList = ['unprivileged','isolated','allow']   #设置特权参数
compressionList = ['none','bzip2','gzip','lzma','xz']   #设置 启用备份  时的 压缩级别
deviceMgtList = ['allow','managed','block']    #设置硬盘设备、网卡设备的 允许、禁用、托管 参数
diskPathList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  #设置云硬盘路径


'''获取区域数据'''
def getDC():
    try:
        DCList = requests.get(url=dcURL ,headers=headers).json()
        return DCList['data']
    except Exception as e:
        print(e)


'''获取最新一条规格信息'''
def getLatestFlavor():
    try:
        res = requests.get(url=flavorMgtUrl,headers=headers).json()
        latestFlavor = res['data'][0]
        return latestFlavor
    except Exception as e:
        print(e)


'''获取业务池列表'''
def getBusiPool(region):
    try:
        headers['region'] = region
        poolListRes = requests.get(url=busiPoolMgtUrl,headers=headers).json()
        return poolListRes
    except Exception as e:
        print(e)


#新建业务池
def creBusiPool(num, regon):
    '''
    :param num:
    :return:
    '''
    try:
        headers = {'Content-Type': 'application/json',
                   'Authorization':token,
                   'region':regon}

        creBusiPoolParam = {
            "name":"AutoBP"+str(num),
            "description":"自动化脚本创建的业务池",
            "limits_cpu":"2",
            "limits_memory":"2",
            "limits_networks":"2",
            "limits_disk":"20",
            "limits_instances":"2",
            "share_store":"20",
            "restricted":random.choice(switch4PoolSecurity),
            "single_storage_pool":"false",
            "restricted_containers_interception":"block"
        }

        #设置开启池安全时的参数
        if creBusiPoolParam['restricted'] == 'true':
            #配置云组件时的参数
            creBusiPoolParam['restricted_cluster_target'] = random.choice(allowBlockList)          #允许指定主机
            creBusiPoolParam['restricted_containers_nesting'] = random.choice(allowBlockList)      #嵌套(PanaOCS)
            creBusiPoolParam['restricted_containers_privilege'] = random.choice(privilegeList)     #特权(PanaOCS)
            creBusiPoolParam['restricted_containers_interception'] = random.choice(allowBlockList)  #系统调用拦截PanaOCS的参数
            creBusiPoolParam['restricted_containers_lowlevel']= random.choice(allowBlockList)       #使用低级选项（PanaOCS）
            if creBusiPoolParam['restricted_containers_lowlevel']=='allow':
                creBusiPoolParam['restricted_idmap_gid'] = random.randint(0,65535)                       #idmap.uid可用范围
                creBusiPoolParam['restricted_idmap_uid'] = random.randint(0, 65535)                      #idmap.gid可用范围
            creBusiPoolParam['restricted_virtual_machines_lowlevel']= random.choice(allowBlockList)  #使用低级选项（PanaVM）

            #配置设备时的参数
            creBusiPoolParam['restricted_devices_disk'] = random.choice(deviceMgtList)              #硬盘设备
            if creBusiPoolParam['restricted_devices_disk'] == 'allow':
                creBusiPoolParam['restricted_devices_disk_paths'] = '/'+(random.choice(diskPathList)+(random.choice(diskPathList)))    #硬盘路径限制
            creBusiPoolParam['restricted_devices_usb'] = random.choice(allowBlockList)               #USB设备
            creBusiPoolParam['restricted_devices_nic'] = random.choice(deviceMgtList)                #网卡设备
            creBusiPoolParam['restricted_devices_pci']  = random.choice(allowBlockList)              #PCI设备
            creBusiPoolParam['restricted_devices_unix_block']  = random.choice(allowBlockList)       #UNIX-BLOCK设备
            creBusiPoolParam['restricted_devices_unix_char']  = random.choice(allowBlockList)       #UNIX-char设备
            creBusiPoolParam['restricted_devices_unix_hotplug']  = random.choice(allowBlockList)     #Unix Hotplug设备
            # creBusiPoolParam['restricted_devices_gpu'] = random.choice(allowBlockList)               #GPU设备

            #配置网络时的参数

            # 配置数据保护时的参数
            creBusiPoolParam['restricted_snapshots'] = random.choice(allowBlockList)  # 启用创建云组件/云硬盘快照

        print("创建业务池的参数为： {}".format(creBusiPoolParam))
        creBusiPoolRes = requests.post(url=busiPoolMgtUrl,headers = headers, json=creBusiPoolParam,verify=False).json()
        if creBusiPoolRes['message']=='success':
            print("*******************成功创建业务池**************************")
        else:
            print("*******************创建业务池失败，响应结果为：{}".format(creBusiPoolRes))
    except Exception as e:
        print(e)


'''批量创建业务池'''
def batchCreBusiPool(num,n,region ):
    for i in range(n):
        creBusiPool(num,region)
        num = num + 1



'''删除业务池'''
def delBusiPool(poolId,region):
    try:
        headers['region']=region
        url = busiPoolMgtUrl + '/' + str(poolId)
        print(url)
        poolDelRes = requests.delete(url=url,headers=headers).json()
        if poolDelRes['code'] == 0:
            print("***************业务池删除成功***************")
        else:
            print("***************业务池删除失败,结果为{}***************".format(poolDelRes))
    except Exception as e:
        print(e)


'''批量删除Auto开头的业务池'''
def batchDelAutoPool(region):
    # 查询业务池中带有Auto字样的业务池
    headers['region'] = region
    data =getBusiPool(region)['data']

    poolIdList = []
    for item in data:
        if 'Auto' in item['name']:
            poolIdList.append(item['id'])
    # 删除业务池
    for poolId in poolIdList:
        delBusiPool(poolId,region)




'''获取某个业务池的安全组数据'''
def getSecurityGroup(poolId):
    try:
        securityGrpList = requests.get(url=securityGrpUrl + '?project_id=' + str(poolId),headers=headers).json()
        return securityGrpList['data']
    except Exception as e:
        print(e)



'''获取用户数据'''
def getUsers():
    try:
        userList = requests.get(url=userMgtUrl ,headers=headers).json()
        return userList['data']
    except Exception as e:
        print(e)


'''创建用户数据，state=0，禁用； state=1，激活'''
def creUsers(n):
    try:
        reqParam ={
                # "username":'uName' + str(random.randint(0,9999)),
                "username": 'uName'+str(n),
                # "username": random.choice(diskPathList) + 'uName' + str(random.randint(0, 9999)),
                "realname":faker.name(),
                "email":faker.free_email(),
                "phone":faker.phone_number(),
                "description":"自动化脚本创建的用户",
                # "state":random.randint(0,2),
                "state": 1,
                "password":"11112222",
                "confirmPassword":"11112222"
            }

        userRes = requests.post(url=userMgtUrl ,headers=headers,json=reqParam,verify=False).json()
        if userRes['message']=='success':
            print("*******************成功创建用户**************************")
        else:
            print("*******************创建用户失败，响应结果为：{}".format(userRes))
        return userRes['data']
    except Exception as e:
        print(e)


'''批量创建用户'''
def batchCreUsers(n,m ):
    for i in range(n,m):
        creUsers(n)
        n=n+1




'''删除未删除的用户数据'''
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



'''删除未删除的用户数据'''
def delAutoUser():
    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}
        Uinfo = getUsers()
        userList = []
        for item in Uinfo:
            if 'uName' in item['username']:
                userList.append(item['id'])
                # 删除用户
                for userId in userList:
                    reqParam ={"id":userList}
                    delUres = requests.post(url=delUserUrl,headers=headers,json=reqParam).json()
                    if delUres['code'] == 0:
                        print('**************{}删除成功**************'.format(id))
                    else:
                        print('**************{}删除失败**************'.format(id))
    except Exception as e:
        print(e)




'''获取用户组数据'''
def getUserGroup():
    try:
        userGroupList = requests.get(url=userGroupMgtUrl ,headers=headers).json()
        return userGroupList['data']
    except Exception as e:
        print(e)


'''创建用户组'''
def creUserGruop():
    try:
        reqParam ={
                "name": "userGroup" + str(random.randint(0,9999)),
                # "name": random.choice(diskPathList) + 'userGroup' + str(random.randint(0, 9999)),
                "description": "自动化脚本创建的用户组"
            }
        userRes = requests.post(url=userGroupMgtUrl ,headers=headers,json=reqParam,verify=False).json()
        if userRes['message']=='success':
            print("*******************成功创建用户组**************************")
        else:
            print("*******************创建用户组失败，响应结果为：{}".format(userRes))
        return userRes['data']
    except Exception as e:
        print(e)



'''删除用户组数据'''
def delUG():

    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}
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



'''删除用户组数据'''
def delUG():
    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}
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


'''获取最新一条秘钥信息'''
def getLatestKey():
    try:
        res = requests.get(url=keyUrl,headers=headers).json()
        latestKey = res['data'][0]
        return latestKey
    except Exception as e:
        print(e)



'''创建池网络'''
def crePriNet(Num):
    try:
        reqParam ={
                "name": "PriNet" + str(Num),
                "type": "Geneve",
                "network": "external",
                "ipv4_address": "10.10.10.10/24",
                "bridge_mtu": 1442
            }
        userRes = requests.post(url=userGroupMgtUrl ,headers=headers,json=reqParam,verify=False).json()
        if userRes['message']=='success':
            print("*******************成功创建用户组**************************")
        else:
            print("*******************创建用户组失败，响应结果为：{}".format(userRes))
        return userRes['data']
    except Exception as e:
        print(e)



'''创建云硬盘'''
def creDataDisk(dcName,projectId,num):
    try:
        headers['region']= dcName
        reqParam ={
                "name":"cd" + str(num),
                "disk_type":"block",  #块类型-block  文件类型-filesystem
                "description":"",
                "pool_id":"LocalZFS",
                "size": str(num),
                "share_vol":"unshare",
                "target":"node-1",
                "project_id":projectId
            }
        creCDRes = requests.post(url=datadiskUrl ,headers=headers,json=reqParam,verify=False).json()

        if creCDRes['message']=='success':
            print("*******************成功创建云硬盘**************************")
        else:
            print("*******************创建云硬盘失败，响应结果为：{}".format(creCDRes))
        return creCDRes['data']
    except Exception as e:
        print(e)


'''批量创建云硬盘'''
def batchCreDataDisk(dcName,projectId,startNum,endNum):
    for i in range(startNum,endNum):
        creDataDisk(dcName,projectId,startNum)
        startNum = startNum + 1


# creDataDisk("qa_dc20","c00571d312064fb5b93a5714cf622d33",8)
batchCreDataDisk("qa_dc20","c00571d312064fb5b93a5714cf622d33",11,22)