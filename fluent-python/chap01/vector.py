#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 12:10
# @Author  : 朱文赵
# @Site    : 
# @File    : vector.py
# @Software: PyCharm

from math import hypot


class Vector:

    """内置函数"""


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
