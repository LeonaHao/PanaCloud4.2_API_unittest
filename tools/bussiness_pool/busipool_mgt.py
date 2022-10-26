# -*- coding: utf-8 -*-
# @Time: 2022/10/24 17:35
# @Author: Leona
# @File: busipool_mgt.py

from configs.url_configs import busiPoolMgtUrl
import requests
from lib.handle_yaml import read_yaml



class BusiPoolMgt():
    token = read_yaml('token.yaml')

    #新建业务池
    def cre_busi_pool(self,num):
        '''
        :param num:
        :return:
        '''
        self.headers = {'Content-Type': 'application/json',
                        'Authorization':self.token}

        creBusiPoolParam = {
            "name":"AutoBP"+str(num),
            "description":"自动化脚本创建的业务池",
            "limits_cpu":"2",
            "limits_memory":"2",
            "limits_networks":"2",
            "limits_disk":"20",
            "limits_instances":"2",
            "share_store":"20",
            "restricted_containers_privilege":"unprivileged",
            "restricted_devices_nic":"managed",
            "restricted_containers_nesting":"block",
            "restricted_devices_disk":"block",
            "restricted_devices_gpu":"block",
            "restricted_devices_usb":"block",
            "restricted_devices_pci":"block",
            "restricted_devices_unix_block":"block",
            "restricted_backups":"allow",
            "backups_compression_algorithm":"xz",
            "restricted_snapshots":"allow",
            "restricted":"true",
            "single_storage_pool":"false",
            "restricted_containers_interception":"block"
        }

        creBusiPoolRes = requests.post(url=busiPoolMgtUrl,headers = self.headers, json=creBusiPoolParam,verify=False).json()
        print(creBusiPoolRes)

if __name__ == '__main__':
    bp = BusiPoolMgt()
    bp.cre_busi_pool(3)

