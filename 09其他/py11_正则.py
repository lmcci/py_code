import re

res = re.match(r'H', 'hello world')
print(res)
# 如果没有匹配 res就是None


# 只有一个数字
res = re.match(r'速度与激情\d', '速度与激情3')
print(res.group())  # 取出匹配的结果

print(re.match(r'速度与激情\d', '速度与激情8800').group())

# [] 表示一位  满足其中有一个
# print(re.match(r'速度与激情[12345678]', '速度与激情9').group())
print(re.match(r'速度与激情[1-8]', '速度与激情8').group())


# 只有一个字符    \w      [0-9a-zA-Z_] 中文 等等  不包括符号
print(re.match(r'速度与激\w', '速度与激情A').group())


# \s 空格 tab

# .  一位任意字符  默认 除了换行 \n   设置re.S可以包括\n  re.match(r'.', '\n', re.S)







#   出现次数    约束前面一位正则

# {1, 2}    出现1到2次  包括左右
# {10}      只出现10次
print(re.match(r'\d{10}', '012345678900').group())

# ? 可以出现1次 或者 0次

# * 可以出现 0-n 次

# + 可以出现 1-n 次





# match自带判断开头

# ^ 以什么开头
# $ 以前一位结尾



# 正则中如果用到 ?+*^$ 要转义  \.


# | 或者   前面能够匹配 或者 后面能够匹配

