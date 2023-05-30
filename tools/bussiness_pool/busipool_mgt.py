# -*- coding: utf-8 -*-
# @Time: 2022/10/24 17:35
# @Author: Leona
# @File: busipool_mgt.py

from conf.url_configs import busiPoolMgtUrl
import requests,random
from lib import handle_yaml
from lib.login import login
from lib.commonPanaCloud import getBusiPool,del_busi_pool

'''将token写入到yaml文件'''
token = {"token":login("admin","P@ssw0rd")}
handle_yaml.write_yaml(token,'token.yaml')

token = handle_yaml.read_yaml('token.yaml')
switch4PoolSecurity = ['true','false']   #设置业务池是否开启池安全
allowBlockList = ['allow','block']    #设置所有  禁用/允许  参数
privilegeList = ['unprivileged','isolated','allow']   #设置特权参数
compressionList = ['none','bzip2','gzip','lzma','xz']   #设置 启用备份  时的 压缩级别
deviceMgtList = ['allow','managed','block']    #设置硬盘设备、网卡设备的 允许、禁用、托管 参数
diskPathList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  #设置云硬盘路径


#新建业务池
def cre_busi_pool(num, regon):
    '''
    :param num:
    :return:
    '''
    try:
        headers = {'Content-Type': 'application/json',
                   'Authorization':token,
                   'region':'regon'}

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



'''删除自动化脚本创建的业务池'''
# def del_busi_pool():
#     # 查询业务池中带有Auto字样的业务池
#     data =getBusiPool()['data']
#     poolIdList = []
#     for item in data:
#         if 'Auto' in item['name']:
#             poolIdList.append(item['id'])
#     # 删除自动化创建的业务池
#     for poolId in poolIdList:
#         del_busi_pool(poolId)





if __name__ == '__main__':

    # cre_busi_pool(3)
    # batch_cre_busi_pool(13,3)

    # 查询业务池中带有Auto字样的业务池
    data =getBusiPool()['data']
    poolIdList = []
    for item in data:


            poolIdList.append(item['id'])

    #查找业务池的id以及业务池内默认安全组的id，以便在底层删除使用,底层通过    ocs project switch {poolId}、   ocs network acl delete  {securityGroupId}
    # for poolId in poolIdList:
    #     securityGroups = getSecurityGroup(poolId)
    #     for sg in securityGroups:
    #         print("业务池{}的安全组有{}".format(poolId,sg['id']))

    # 删除业务池
    for poolId in poolIdList:
        del_busi_pool(poolId)



