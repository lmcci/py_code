# *-* coding:utf-8 *-*
# py2.x 文件头部加上指定编码 才能正常支持中文  （文件编码）

# 但是对字符串处理 也会以一个字符串处理  比如遍历字符串  （字符串编码）
# 在字符串前面加 u 可以解决字符串编码问题
test_str = u'你好世界'

print("hello world")
print("hello python")

print("你好 世界， python2.x版本不支持中文, python3.x支持中文")
print("SyntaxError: Non-ASCII character")
# python2.6/2.7 完全支持python2.x语法 部分支持python3.x语法
# python3.x 不支持python2.x语法

# 2008年出的py3.x

print("aaa")
print("aaa")

# 每行代码只完成一个动作 上面两个print不能写在同一行
# 不能有多余的缩进

# 解释器 官方使用C语言开发 CPython
# 还有java版本 .net版本 py版本

# 更改项目的解释器  setting -- Project:XX -- project interpreter

# 文件名 小写字母 数字 下划线  不能以数字开头
