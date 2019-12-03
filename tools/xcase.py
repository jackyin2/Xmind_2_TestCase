#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author  : Jack
# @FileName: xcase.py
# @Time    : 2019/12/2 17:51

class XmindCase():
    def __init__(self):
        self.testcode=None
        self.model=None
        self.function=None
        self.title = None
        self.step = None
        self.expect=None
        self.result=None
        self.notes=None
        self.priority=None

    def set_priority(self, v):
        self.priority = v

    def set_testcode(self, v):
        self.testcode = v

    def set_function(self, v):
        self.function = v

    def set_notes(self,  v):
        self.notes = v

    def set_title(self, v):
        self.title = v

    def set_model(self, v):
        self.model = v

    def set_step(self, v):
        self.step = v

    def set_result(self, v):
        self.result = v

    def set_expect(self, v):
        self.expect = v

