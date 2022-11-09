# -*- coding: utf-8 -*-
# @Time: 2022/10/24 17:35
# @Author: Leona
# @File: busipool_mgt.py

from conf.url_configs import busiPoolMgtUrl
import requests,random
from lib.handle_yaml import read_yaml
from lib.commonPanaCloud import getBusiPool,getSecurityGroup

token = read_yaml('token.yaml')
switch4PoolSecurity = ['true','false']   #设置业务池是否开启池安全
allowBlockList = ['allow','block']    #设置所有  禁用/允许  参数
privilegeList = ['unprivileged','isolated','allow']   #设置特权参数
compressionList = ['none','bzip2','gzip','lzma','xz']   #设置 启用备份  时的 压缩级别
deviceMgtList = ['allow','managed','block']    #设置硬盘设备、网卡设备的 允许、禁用、托管 参数
diskPathList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  #设置云硬盘路径

#新建业务池
def cre_busi_pool(num):
    '''
    :param num:
    :return:
    '''
    try:
        headers = {'Content-Type': 'application/json',
                        'Authorization':token}
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
            creBusiPoolParam['restricted_containers_nesting'] = random.choice(allowBlockList)
            creBusiPoolParam['restricted_containers_privilege'] = random.choice(privilegeList)
            creBusiPoolParam['restricted_backups'] = random.choice(allowBlockList)
            if creBusiPoolParam['restricted_backups'] == 'allow':
                creBusiPoolParam['backups_compression_algorithm'] = random.choice(compressionList)
            creBusiPoolParam['restricted_snapshots']= random.choice(allowBlockList)
            creBusiPoolParam['restricted_devices_disk'] = random.choice(deviceMgtList)
            if creBusiPoolParam['restricted_devices_disk'] == 'allow':
                creBusiPoolParam['restricted_devices_disk_paths'] = '/'+(random.choice(diskPathList)+(random.choice(diskPathList)))
            creBusiPoolParam['restricted_devices_gpu'] = random.choice(allowBlockList)
            creBusiPoolParam['restricted_devices_usb'] = random.choice(allowBlockList)
            creBusiPoolParam['restricted_devices_nic'] = random.choice(deviceMgtList)
            creBusiPoolParam['restricted_devices_pci']  = random.choice(allowBlockList)
            creBusiPoolParam['restricted_devices_unix_block']  = random.choice(allowBlockList)
            creBusiPoolParam['restricted_devices_pci']  = random.choice(allowBlockList)
            #缺少系统调用拦截PanaOCS的参数

            # 设置池数据保护的参数------目前未实现

        print("创建业务池的参数为： {}".format(creBusiPoolParam))
        creBusiPoolRes = requests.post(url=busiPoolMgtUrl,headers = headers, json=creBusiPoolParam,verify=False).json()
        if creBusiPoolRes['message']=='success':
            print("*******************成功创建业务池**************************")
        else:
            print("*******************创建业务池失败，响应结果为：{}".format(creBusiPoolRes))
    except Exception as e:
        print(e)

'''批量创建业务池'''
def batch_cre_busi_pool(num,n ):
    for i in range(n):
        cre_busi_pool(num)
        num = num + 1




'''删除业务池'''
def del_busi_pool(poolId):
    try:
        headers = {'Content-Type': 'application/json',
                   'Authorization': token}
        url = busiPoolMgtUrl + '/' + str(poolId)
        print(url)
        poolDelRes = requests.delete(url=url,headers=headers).json()
        if poolDelRes['code'] == 0:
            print("***************业务池删除成功***************")
        else:
            print("***************业务池删除失败,结果为{}***************".format(poolDelRes))
    except Exception as e:
        print(e)


if __name__ == '__main__':

    # cre_busi_pool(3)
    # batch_cre_busi_pool(13,3)

    #查询业务池中带有Auto字样的业务池
    data =getBusiPool()['data']
    poolIdList = []
    for item in data:
        if 'Auto' in item['name']:
            poolIdList.append(item['id'])

    print(poolIdList)
    #查找业务池的id以及业务池内默认安全组的id，以便在底层删除使用,底层通过    ocs project switch {poolId}、   ocs network acl delete  {securityGroupId}
    # for poolId in poolIdList:
    #     securityGroups = getSecurityGroup(poolId)
    #     for sg in securityGroups:
    #         print("业务池{}的安全组有{}".format(poolId,sg['id']))

    # 删除业务池
    for poolId in poolIdList:
        del_busi_pool(poolId)




