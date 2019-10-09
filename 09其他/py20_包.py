# 包 就是一个目录  包含多个模块  必须有一个文件 __init__.py

# 命名 小写字母 下划线 数字 不以数字开头

# import 包名  导入包中的所有模块


import package_test

print(dir(package_test))

package_test.send_msg.send('hello')
package_test.receive_msg.receive()


# 打包 安装包 见课件
