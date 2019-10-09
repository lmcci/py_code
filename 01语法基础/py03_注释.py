# 单行注释以#开头

print("hello world")  # 写在同一行间隔两个空格

"""
    三个引号 多行注释
    
    （不可嵌套 不可以有三个引号）
"""

'''
    单引号双引号都可以
'''


def fun():
    """在函数定义的下方 是 文档注释 需要用两个双引号"""

    print('hello world')


# 光标选中fun  在菜单栏 view -- QuickDocument 可查看函数的文档注释
fun()
