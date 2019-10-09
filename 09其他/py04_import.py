import sys

print(sys.path)
# ['/Users/lmcci/PycharmProjects/PythonProject/0223',
#  '/Users/lmcci/PycharmProjects/PythonProject',
#  '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
#  '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
#  '/Users/lmcci/PycharmProjects/PythonProject/venv/lib/python3.7/site-packages',
#  '/Users/lmcci/PycharmProjects/PythonProject/venv/lib/python3.7/site-packages/setuptools-39.1.0-py3.7.egg',
#  '/Users/lmcci/PycharmProjects/PythonProject/venv/lib/python3.7/site-packages/pip-10.0.1-py3.7.egg',
#  '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']

# import 路径  的先后顺序
# 可以对sys.path进行更改 .append() 来更改模块引入的顺序 和 路径


# 重新导入模块
# 为了防止模块重复导入 如果导入过就用以前的  比如发版的时候程序要一直运行 只更新其中一个模块
from imp import reload
reload(sys)


# import 模块名
# import 模块名1, 模块名2, 模块名3
# import 模块名 as 别名
#
# from 模块名 import 变量名
# from 模块名 import 变量名1, 变量名2
# from 模块名 import *



# notice 多个模块引入一个模块来共享数据的时候 如果其中一个要对共享模块的数据进行更改的时候
# 要使用 import 共享模块名   的方式导入  共享模块名.变量名 = xxx
# 如果是用 from 共享模块名 import 变量名 （变量名 = 123）的方式来修改共享变量 修改的是模块内的全局变量而不是共享模块的变量


