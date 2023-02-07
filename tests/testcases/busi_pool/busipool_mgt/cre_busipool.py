# -*- coding: utf-8 -*-
# @Time: 2022/10/31 10:54
# @Author: Leona
# @File: cre_busipool.py

import requests
import json
import random
from lib.my_unit import MyUnit
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from conf.url_configs import busiPoolMgtUrl
from lib.commonPanaCloud import getDC


"""
管理视图》业务池》新建业务池
"""


class CreBusiPool(MyUnit):
    """管理视图》业务池》新建业务池"""

    switch4PoolSecurity = ['true', 'false']  # 设置业务池是否开启池安全
    allowBlockList = ['allow', 'block']  # 设置所有  禁用/允许  参数
    privilegeList = ['unprivileged', 'isolated', 'allow']  # 设置特权参数
    compressionList = ['none', 'bzip2', 'gzip', 'lzma', 'xz']  # 设置 启用备份  时的 压缩级别
    deviceMgtList = ['allow', 'managed', 'block']  # 设置硬盘设备、网卡设备的 允许、禁用、托管 参数
    diskPathList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']  # 设置云硬盘路径
    global regionInfo
    regionInfo = getDC()


    def getTest(self, tx):
        logger.info("****************创建业务池接口开始****************")
        self.headers['region'] = regionInfo[0]['name']
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqParam['restricted']=  random.choice(self.switch4PoolSecurity)
        
        #设置开启池安全时的参数
        if reqParam['restricted'] == 'true':
            #配置云组件时的参数
            reqParam['restricted_cluster_target'] = random.choice(self.allowBlockList)          #允许指定主机
            reqParam['restricted_containers_nesting'] = random.choice(self.allowBlockList)      #嵌套(PanaOCS)
            reqParam['restricted_containers_privilege'] = random.choice(self.privilegeList)     #特权(PanaOCS)
            reqParam['restricted_containers_interception'] = random.choice(self.allowBlockList)  #系统调用拦截PanaOCS的参数
            reqParam['restricted_containers_lowlevel']= random.choice(self.allowBlockList)       #使用低级选项（PanaOCS）
            if reqParam['restricted_containers_lowlevel']=='allow':
                reqParam['restricted_idmap_gid'] = random.randint(0,65535)                       #idmap.uid可用范围
                reqParam['restricted_idmap_uid'] = random.randint(0, 65535)                      #idmap.gid可用范围
            reqParam['restricted_virtual_machines_lowlevel']= random.choice(self.allowBlockList)  #使用低级选项（PanaVM）

            #配置设备时的参数
            reqParam['restricted_devices_disk'] = random.choice(self.deviceMgtList)              #硬盘设备
            if reqParam['restricted_devices_disk'] == 'allow':
                reqParam['restricted_devices_disk_paths'] = '/'+(random.choice(self.diskPathList)+(random.choice(self.diskPathList)))    #硬盘路径限制
            reqParam['restricted_devices_usb'] = random.choice(self.allowBlockList)               #USB设备
            reqParam['restricted_devices_nic'] = random.choice(self.deviceMgtList)                #网卡设备
            reqParam['restricted_devices_pci']  = random.choice(self.allowBlockList)              #PCI设备
            reqParam['restricted_devices_unix_block']  = random.choice(self.allowBlockList)       #UNIX-BLOCK设备
            reqParam['restricted_devices_unix_char']  = random.choice(self.allowBlockList)       #UNIX-char设备
            reqParam['restricted_devices_unix_hotplug']  = random.choice(self.allowBlockList)     #Unix Hotplug设备
            # reqParam['restricted_devices_gpu'] = random.choice(self.allowBlockList)               #GPU设备

            #配置网络时的参数

            # 配置数据保护时的参数
            reqParam['restricted_snapshots'] = random.choice(self.allowBlockList)  # 启用创建云组件/云硬盘快照


            # reqParam['restricted_backups'] = random.choice(self.allowBlockList)                 #启用备份
            # if reqParam['restricted_backups'] == 'allow':
            #     reqParam['backups_compression_algorithm'] = random.choice(self.compressionList)  #备份压缩级别

        
        if flag == 0:
            self.headers['Authorization'] = ''
        if flag == 1:
            reqParam['name'] = reqParam['name'] + "_rand_" + str(random.randint(1,1000))
        if flag == 2:
            reqParam['restricted'] = 'false'
        if flag == 3:
            reqParam['restricted'] = 'true'
            reqParam['restricted_devices_disk'] = 'allow'
            if caseNum == '051':
                reqParam['restricted_devices_disk_paths'] = ''
            if caseNum == '052':
                reqParam['restricted_devices_disk_paths'] = '/1,/2,/3,/4,/5,/6,/7,/8,/9,/10,/11,/12,/13,/14,/15,/16,/17,/18,/19,/20,/21,/22,/23,/24,/25,/26,/27,/28,/29,/30,/31,/32,/33,/34,/35,/36,/37,/38,/39,/40,/41,/42,/43,/44,/45,/46,/47,/48,/49,/50,/51,/52,/53,/54,/55,/56,/57,/58,/59,/60,/61,/62,/63,/64,/65,/66,/67,/68,/69,/70,/71,/72,/73,/74,/75,/76,/77,/78,/79,/80,/81,/82,/83,/84,/85,/86,/87,/88,/89,/90,/91,/92,/93,/94,/95,/96,/97,/98,/99,/100'
            if caseNum == '053':
                reqParam['restricted_devices_disk_paths'] = '/1,/2,/3,/4,/5,/6,/7,/8,/9,/10,/11,/12,/13,/14,/15,/16,/17,/18,/19,/20,/21,/22,/23,/24,/25,/26,/27,/28,/29,/30,/31,/32,/33,/34,/35,/36,/37,/38,/39,/40,/41,/42,/43,/44,/45,/46,/47,/48,/49,/50,/51,/52,/53,/54,/55,/56,/57,/58,/59,/60,/61,/62,/63,/64,/65,/66,/67,/68,/69,/70,/71,/72,/73,/74,/75,/76,/77,/78,/79,/80,/81,/82,/83,/84,/85,/86,/87,/88,/89,/90,/91,/92,/93,/94,/95,/96,/97,/98,/99,/100,/101'

        logger.info("*******测试数据： " + str(reqParam))

        result = requests.post(url=busiPoolMgtUrl, headers=self.headers, json=reqParam, verify=False).json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************创建业务池接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


__generateTestCases(CreBusiPool, "busipoolMgtData.xlsx", "creBusiPool")

if __name__ == '__main__':
    MyUnit.main()
