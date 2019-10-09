# 文件中的 变量 函数 类 都可以向外界提供
# 模块名 不要和系统提供的重名

import py01
import py02

py01.say_hello()

dog = py02.Dog()

# 如果文件名太长 可以 起别名  模块的别名用大驼峰 只是在当前模块的变量名 他其实的模块名还是原来的

import py03 as ChangeName

ChangeName.test()


# 从模块中导入部分工具  从哪个模块导入哪个工具
# 如果从两个不同的模块中导入了相同名字的函数 后面导入的会覆盖前面导入的

from py04 import Cat
from py05 import Cat as CatModule
from py06 import *


c = Cat()


# 导入模块 搜索文件的顺序
# 1 在当前目录搜索 有就导入
# 2 系统目录搜索


# 每个模块都有一个内置属性 __file__ 文件的路径
# __name__ 如果被导入了就是模块名 如果是当前运行的就是'__main__'


# 模块被导入的时候 会执行所有函数外部的代码




