#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author  : Jack
# @FileName: xmind_parse.py
# @Time    : 2019/11/26 10:04
import xmind
from tools import xcase

l = []

class Xmind(object):
    def __init__(self, xmind_path):
        self.xmind_path = xmind_path
        self.workbook = xmind.load(xmind_path)
        self.sheet = self.workbook.getPrimarySheet()
        self.xmind_sheet_data = self.xmind2dict()
        # # 根节点相关信息
        # self.sheet_topic = self.xmind_sheet_data["topic"]
        # # 模块节点相关信息
        # self.model_topics = self.sheet_topic["topics"]

    def xmind2dict(self):
        self.sheet = self.workbook.getPrimarySheet()
        self.xmind_sheet_data =  self.sheet.getData()
        return self.xmind_sheet_data
        # self.xminddata = self.workbook.to_prettify_json()


    def xmind2case(self):
        models = self.xmind_sheet_data["topic"]['topics']
        global l
        for model in models:
            # 如果存在优先级9，那么则忽略当前的内容
            if 'priority-9' in model['markers'] : continue
            for func in model['topics']:
                if 'priority-9' in func['markers']: continue
                for ca in func['topics']:
                    if 'priority-9' in ca['markers']: continue
                    case = xcase.XmindCase()
                    # 设置模块
                    case.set_model(model['title'])
                    # 设置功能
                    case.set_function(func['title'])
                    # 设置用例
                    case.set_title(ca['title'])

                    # 判断该case的优先级，并设置
                    if ca['markers']:
                        case.set_priority(ca['markers'][0])
                    case.set_step(ca['topics'][0]['title'])

                    # 判断当前的case中的期望结果是否达到预期
                    if 'symbol-right' in ca['topics'][0]['topics'][0]['markers']:
                        case.set_result('Pass')
                    elif 'symbol-wrong' in ca['topics'][0]['topics'][0]['markers']:
                        case.set_result('Fail')
                    elif ca['topics'][0]['topics'][0]['markers'] == []:
                        case.set_result('None')

                    # 设置期望值
                    case.set_expect(ca['topics'][0]['topics'][0]['title'])

                    # 判断备注是否有，如果没有该节点则默认为空，有则赋值topics下的title
                    if len(ca['topics'][0]['topics'][0]['topics']) > 0:
                        case.set_notes(ca['topics'][0]['topics'][0]['topics'][0]['title'])
                    else:
                        case.set_notes('')
                    l.append(case)


if __name__ == "__main__":
    xml = Xmind('E:\jackstudy\Xmind_2_TestCase\\xmind\SCA项目测试用例.xmind')
    print(xml.xmind2dict())
    xml.xmind2case()
    for i in l:
        print(i.title)


    # print(xml.sheet_topic)
    # print(xml.model_topics)










