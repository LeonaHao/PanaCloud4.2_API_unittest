# -*- coding: utf-8 -*-
# @Time: 2022/10/18 15:14
# @Author: Leona
# @File: gen_cidr.py

# 首先引入netaddr
import netaddr

def gen_cidr(startIp,endIp):
    '''
    :param startIp: 开始ip
    :param endIp: 结束ip
    :return: ip列表
    '''
    try:
        #创建一个空的列表，用来装cidr地址
        iplist = []
        # 确定起始和结尾IP，无论多复杂都可以转换
        startip = startIp
        endip = endIp
        #生成一个cidr列表，列表中元素类型为： class 'netaddr.ip.IPNetwork'
        cidrs = netaddr.iprange_to_cidrs(startip, endip)
        #通过enumerate函数，将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，最终返回 enumerate(枚举) 对象
        for k, v in enumerate(cidrs):
            iplist.append(str(v))
        return iplist
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(gen_cidr('192.16.16.10','192.16.246.246'))