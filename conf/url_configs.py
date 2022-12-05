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

'''关于'''
aboutUrl = baseUrl + '/about/'

'''密钥管理'''
keyUrl = baseUrl + '/secret_key/'
delKeyUrl = baseUrl + '/delete_secret/'



'''业务池管理'''
busiPoolMgtUrl = baseUrl + '/projects'

'''存储池管理'''
storPoolMgtUrl = baseUrl + '/storage-pools'


'''规格管理'''
flavorMgtUrl = baseUrl + '/flavors'
delFlavorUrl = baseUrl + '/flavors/batch-delete'


'''身份管理》用户管理'''
userMgtUrl =  baseUrl + '/users'
delUserUrl =  baseUrl + '/users_delete/'
setUserPwdUrl = baseUrl + '/users/set_pwd/'

'''身份管理》用户组管理'''
userGroupMgtUrl =  baseUrl + '/user_group/'
addGroupMemberUrl = baseUrl + '/group_member/'
removeGroupMemberUrl = baseUrl + '/group_member_delete/'

'''身份管理》角色管理'''
roleMgtUrl = baseUrl + '/roles'



'''云中心》镜像'''
mirrorUrl = baseUrl + '/images'

'''安全组'''
securityGrpUrl = baseUrl + '/network-acls'