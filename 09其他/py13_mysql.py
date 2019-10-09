# sql不区分大小写


# mysql -u root -p

# .sql  --是注释

show databases;  查看所有的库

select now();   显示当前时间

select version();   显示当前版本

create database 库名 charset=utf8      创建数据库
show create database 库名     查看创建数据库

drop database 库名    删除数据库


#########################

use 库名  使用/切换 数据库

select database()     查看当前使用的哪个库

#########################

show tables;    查看当前库的表

create table 表名 （字段 类型 约束，xxxxx）

desc 表名     查看表结构

show create table 表名    查看创建表语句








