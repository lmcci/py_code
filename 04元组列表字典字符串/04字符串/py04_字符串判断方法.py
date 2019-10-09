# 中文算作字母

# 判断是否只包含空白字符 空格 \t \n \r
# test_str = ' \t\n\r'
# print(test_str.isspace())

# 所有字符都是字母或者数字
# test_str = '13asdf我'
# print(test_str.isalnum())

# 所有字符都是字母
# test_str = "aaaa我"
# print(test_str.isalpha())

# 所有字符全是数字 不能判断小数
# test_str = '1232321'
# print(test_str.isdecimal())
# 所有字符全是数字 不能判断小数 如果是unicode编码的数字 多少的平方 之类的数字是可以判断的
# test_str = '\u00b2'
# print(test_str.isdigit())
# 所有字符全是数字 除了isdigit的能力 还能判断中文数字
test_str = '一千'
print(test_str.isnumeric())

# 是否是标题格式 单词首字母大写 单词边界后一个字母大写
# test_str = 'Helloaaa E我是'
# print(test_str.istitle())

# 所有字符全是大写
# test_str = 'HELLO我'
# print(test_str.isupper())

# 所有字符全是小写
# test_str = 'hello我'
# print(test_str.islower())
