#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author  : Jack
# @FileName: xm2ex.py
# @Time    : 2019/11/25 18:09



# def gen_my_xmind_file():
#     # 1、如果指定的XMind文件存在，则加载，否则创建一个新的
#     workbook = xmind.load("my.xmind")
#
#     # 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
#     sheet1 = workbook.getPrimarySheet()
#     # 对第一个画布进行设计完善，具体参照下一个函数
#     design_sheet1(sheet1)
#
#     # 3、创建第二个画布
#     gen_sheet2(workbook, sheet1)
#
#     # 4、保存（如果指定path参数，另存为该文件名）
#     xmind.save(workbook, path='test.xmind')

#
# import xmind
# workbook = xmind.load('E:\jackstudy\Xmind_2_TestCase\\xmind\SCA项目测试用例.xmind')
# print(workbook.getData())
# # print(workbook.to_prettify_json())
# sheet = workbook.getPrimarySheet()
# topic = sheet.getRootTopic()
# print(topic.getData())
#
# def get_topic(wb):
#     pass

import argparse
from tools import excel, xmind_parse

# 1 解析xmind内容
xm = xmind_parse.Xmind('E:\jackstudy\Xmind_2_TestCase\\xmind\SCA项目测试用例.xmind')
xm.xmind2case()

# 2 创建excel
with excel.ExcelWriter('xxx.xlsx') as ew:
    ew.init_title()
    ew.write_rows()




