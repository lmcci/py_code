# 一对单引号 一对双引号 都可以定义一个字符串
# 可以看成一个字符序列

str_1 = "hello world"

# 取的某个索引对应的字符
# print(str[2])

# 遍历字符串
# for s in str:
#     print(s)


test_str = 'hello world'

# 字符串长度
print(len(test_str))

# 字符出现的次数 如果不存在返回0
print(test_str.count('l'))

# 字符第一次出现的索引 不存在就报错
print(test_str.index('l'))

# 是否只有空格 \t \n \r
print('  \t  '.isspace())

# 是否只有字母 无法判断中文
print('aaaaasdflkjLAKJSF'.isalpha())

# 是否值有数字和字母 无法判断中文
print('klajsdklfjalks23121'.isalnum())

# 每个单词首字母大写 单词边界分割
print('Lkasjf-Lakjsf_Asdfk Ssadfaf'.istitle())

# 是否字母都小写/大写
print('asdasdf'.islower())
print('ASDFASDF'.isupper())

# num_str = '1.2' # 都不能判断小数
# num_str = '(1)'  # unicode
num_str = '一千'

num_str.isdecimal()  # 弱
num_str.isdigit()  # 中
num_str.isnumeric()  # 强


