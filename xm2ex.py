#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author  : Jack
# @FileName: xm2ex.py
# @Time    : 2019/11/25 18:09


import argparse
from tools import excel, xmind_parse

# 1 解析xmind内容
xm = xmind_parse.Xmind('E:\jackstudy\Xmind_2_TestCase\\xmind\SCA项目测试用例.xmind')
xm.xmind2case()

# 2 创建excel
with excel.ExcelWriter('xxx.xlsx') as ew:
    ew.init_title()
    ew.write_rows()





