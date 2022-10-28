# -*- coding: utf-8 -*-
# @Time: 2022/10/24 14:03
# @Author: Leona
# @File: handle_param.py


def param_csombine(**kwargs):
    a = ""
    # x是key值，y是value值, 通过循环，拼接参数
    for x, y in kwargs.items():
        a += "%s=%s" % (x, y) + "&"
    # return时要剔除最后的&符号
    return a[0:len(a) - 1]


