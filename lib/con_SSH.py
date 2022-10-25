# -*- coding: utf-8 -*-
# @Time: 2022/10/18 14:45
# @Author: Leona
# @File: con_SSH.py

import paramiko

#定义SSH连接方法
def con_SSH(hostIp,username,password,cmd,port=22):
    '''
    :param hostIp: 节点IP
    :param port: 节点端口
    :param username:用户名
    :param password:密码
    :param cmd:要执行的命令
    :return:
    '''
    #定义连接重试次数
    try_times = 3
    try:
        #实例化一个SSHClient对象
        ssh = paramiko.SSHClient()
        #自动添加策略，保存服务器的主机名和秘钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接SSH服务器，传参为： 服务器地址，端口，用户名，密码
        ssh.connect(hostname=hostIp,port=port, username=username,password=password)
        #打开一个channel并执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        #打印执行结果到控制台
        print((stdout.read().decode('utf-8')))


    except Exception as e:
        if try_times != 0:
            print('连接%s失败， 进行重试' % hostIp)
            try_times -= 1
        else:
            print('连接3次失败， 结束程序')
            exit(1)



# con_SSH("192.168.7.231","root","Admin@9000",'lscpu | grep -E "Architecture:|CPU\(s\):|Model name:"')