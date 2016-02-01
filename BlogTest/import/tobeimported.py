#-*- coding:utf8 -*-
"""
import测试，被导入文件
"""
print('begin in module -->',__name__)

import sys
print(__name__,' in sys.modules -->',__name__ in sys.modules)
#被其他文件导入将输出 True，而单独执行本文件则为 False

import tobeimported

base = set(dir(sys.modules[__name__]))
x = 1
print(set(dir(sys.modules[__name__]))-base)
#执行代码时刻增加对象，执行结果应该为刚刚创建的 base 和 x
print('end in module -->',__name__)
