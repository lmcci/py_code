# 是否以指定字符串开始
test_str = 'hello world'

print(test_str.startswith('hel'))


# 是否以指定字符串结束
print(test_str.endswith('ld'))


# 查找子字符串 返回出现的索引位置
# # find  index 区别  指定的子之付出不存在 find返回-1 index报错
print(test_str.find('llo'))


# 替换字符串 返回替换后的字符串 对原来的字符串不更改
print(test_str.replace('hello', '你好'))
print(test_str)


# 文本对齐 对左右添加字符串（默认英文空格可指定）  以居中 或者 左对齐 右对齐
str1 = 'asdf'
str2 = 'akasdfklajsdfl'
str3 = 'sdfasdf'
str4 = 'a'
str5 = 'lkajsdkljflkasjdflkj'

print(str1.center(20, 'a'))
print(str2.center(20, 'a'))
print(str3.center(20))
print(str4.ljust(20))
print(str5.rjust(20))


# 去除空白字符 空格 \t \r \n  不会对原字符串更改
test_str = '  122 '
print(test_str.strip())
print(test_str.lstrip())
print(test_str.rstrip())

print(test_str)

