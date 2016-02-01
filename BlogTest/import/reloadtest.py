#-*- coding: utf8 -*-
"""
reload测试
"""
#----- 被导入代码 reloadImported.py ------

#----- 测试代码 test.py --------
sep = ': '
print('---- import module ----')
import reloadImported
from reloadImported import x
print(' id(reloadImported)', id(reloadImported), sep=sep)
print(' id(reloadImported.x)', id(reloadImported.x), sep=sep)
print(' id(reloadImported.y)', id(reloadImported.y), sep=sep)
print(' id(x)', id(x), sep=sep)

print('---- reload module ----')
from importlib import reload
reload(reloadImported)
print(' id(reloadImported)', id(reloadImported), sep=sep)
print(' id(reloadImported.x)', id(reloadImported.x), sep=sep)
print(' id(reloadImported.y)', id(reloadImported.y), sep=sep)
print(' id(x)', id(x), sep=sep)
from reloadImported import x
print(' new x id(x)', id(x), sep=sep)

