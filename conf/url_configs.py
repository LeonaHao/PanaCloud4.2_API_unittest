# -*- coding: utf-8 -*-
# @Time: 2022/10/18 14:14
# @Author: Leona
# @File: url_configs.py

'''
配置系统中需要的url地址信息
'''


'''基础地址'''
# baseUrl= 'http://192.168.7.231/1.0'
baseUrl= 'http://192.168.7.75/1.0'

'''登录接口'''
loginUrl = baseUrl+'/login'
'''退出登录接口'''
logoutUrl = baseUrl + '/logout'


'''业务池管理'''
busiPoolMgtUrl = baseUrl + '/projects'


'''规格管理'''
flavorMgtUrl = baseUrl + '/flavors'