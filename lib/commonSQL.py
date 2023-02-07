# -*- coding: utf-8 -*-
# @Time: 2022/10/24 14:00
# @Author: Leona
# @File: commonSQL.py

from lib.MySQLHelper import MySQLHelper


#获取最近一条规格信息
def get_latest_sysFlavor():
    sql = 'select * from sys_flavor order by created_at desc limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res

#获取最早一条规格信息
def get_old_sysFlavor():
    sql = 'select * from sys_flavor order by created_at asc limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res

#获取最近一条用户信息
def get_latest_user():
    sql = 'select * from profile_user where is_delete=0 order by created_at desc limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res


#获取所有未被删除的用户信息
def get_userIds():
    sql = 'select id from profile_user where is_delete=0;'
    param = ()
    res = MySQLHelper('panacloud').get_many(sql,param)
    return res

#获取所有未被删除的用户组信息
def get_userGroupIds():
    sql = 'select id from profile_user_groups where is_delete=0;'
    param = ()
    res = MySQLHelper('panacloud').get_many(sql,param)
    return res


#获取最近一条用户组信息
def get_latest_group():
    sql = 'select * from profile_user_groups where is_delete=0 order by created_at Desc limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res

#获取最近一条用户组成员关系信息
def get_latest_group_member():
    sql = 'select * from profile_user_groups_member order by created_at Desc limit 1;'
    param = ()
    res = MySQLHelper('panacloud').get_one(sql,param)
    return res






