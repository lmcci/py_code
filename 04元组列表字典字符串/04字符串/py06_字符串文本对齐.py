# 向字符串左右添加指定内容 使字符串居中 不会改变原有字符串

test_str = "hello"

print(test_str.center(10, "\t"))
print(test_str)

print(test_str.ljust(10, "\t"))
print(test_str.rjust(10, "\t"))
