# -*- coding: utf-8 -*-
# @Time: 2022/10/24 14:00
# @Author: Leona
# @File: commonSQL.py

from lib.MySQLHelper import MySQLHelper


#获取最近一条规格信息
def get_latest_flavor():
    sql = 'select * from sys_flavor order by created_at limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res

