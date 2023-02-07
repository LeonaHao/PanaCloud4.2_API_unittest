# -*- coding: utf-8 -*-
# @Time: 2022/10/18 14:14
# @Author: Leona
# @File: url_configs.py

'''
配置系统中需要的url地址信息
'''


'''基础地址'''
# baseUrl= 'http://172.16.80.1/1.0'
# baseUrl= 'http://172.16.16.1/1.0'
baseUrl= 'http://172.16.20.1/1.0'                   #基础地址配置变更后，要同步更新base_config中数据库的地址



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
busiPoolUserUrl = baseUrl + '/pool_user'          #业务池成员


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



'''运维管理》数据中心'''
dcURL = baseUrl + '/datacenters'

'''运维管理》节点管理'''
nodeURL = baseUrl + '/ops/nodes'


'''运维管理》基础网络》外部网络'''
basicNetworkURL = baseUrl + '/basic-network'
exNetUrl = baseUrl +'/external-networks'
sysNetUrl = baseUrl +'/ops/system-networks'

'''存储池管理'''
storPoolMgtUrl = baseUrl + '/storage-pools'


'''系统设置》规格管理'''
flavorMgtUrl = baseUrl + '/flavors'
delFlavorUrl = baseUrl + '/flavors/batch-delete'

'''系统设置》授权管理'''
licenseUrl = baseUrl + '/license'
licenseCodeUrl = baseUrl + '/license/code'   #获取机器码

'''系统设置》安全设置'''
ukeyUrl = baseUrl + '/ukey/'


'''日志管理》登录日志'''
loginLogUrl = baseUrl +'/login-logs'

'''日志管理》操作日志'''
operateLogUrl = baseUrl +'/operation-logs'


'''业务视图》云中心》镜像'''
mirrorUrl = baseUrl + '/images'



'''业务视图》智能存储》数据盘'''
datadiskUrl = baseUrl + '/volumes'

'''安全组'''
securityGrpUrl = baseUrl + '/network-acls'


