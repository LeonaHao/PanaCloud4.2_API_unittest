# -*- coding: utf-8 -*-
# @Time: 2022/10/21 15:22
# @Author: Leona
# @File: handle_yaml.py

import os
import yaml
from conf.base_config import libPath

#读取yaml文件中的token
def read_yaml(yamlFile="token.yaml"):
     with open(os.path.join(libPath,yamlFile),'r') as f:
         tokenCont = f.read()
         token = yaml.safe_load(tokenCont)
         return token['token']


#将token写入yaml文件
def write_yaml(cont,yamlFile="token.yaml"):
    with open(os.path.join(libPath, yamlFile), 'w') as f:
        yaml.dump(cont, f)



