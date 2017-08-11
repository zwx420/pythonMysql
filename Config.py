#!/usr/bin/python
# --*-- coding:utf-8 --*--


maxconnections = 500
# 最大的连接数
maxcached = 10
# 最大的空闲连接数
mincached = 5
# 最小的空闲连接数
# blocking = True
# 当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错
# maxshared = 500
# 当连接数达到这个数，新请求的连接会分享已经分配出去的连接
host = "192.168.117.35"
# mysql主机ip
user = "root"
# mysql用户名
passwd = "root"
# 密码
db = "mydb"
# 数据库名
port = 3306
# 端口
use_uni = False
# 是否使用Unicode字符集
dbchar = "utf8"
# 字符集编码

