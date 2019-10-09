try:
    num = int(input('输入一个数字'))
    num = 8 / num
except ValueError as err:
    print(err.args)
    print(type(err))
    print('请输入一个正确的数字')
except(ZeroDivisionError, ArithmeticError):
    print('除0了')
except Exception as err:
    a = err.args
    print('未知错误')
else:
    print('else  没有抛出异常就执行else')
finally:
    print('finally 无论是否出错都执行finally')

print('end')


# 正常: try == else == finally
# 异常: try == except == finally


# 异常的传递 当函数执行时出现异常 会把异常传递给调用的地方  直到传递到主程序 如果还没有处理异常 程序才会终止


# 主动抛出异常

def demo():
    print('demo')
    raise Exception('主动抛出异常')


try:
    demo()
except Exception as err:
    print(err)
