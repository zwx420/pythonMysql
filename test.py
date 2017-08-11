#!/usr/bin/python
# --*-- coding:utf-8 --*--


from MySqlConn import Mysql
from _sqlite3 import Row

# 申请资源
mysql = Mysql()

'''插入'''
insertSql = "insert into t_role(roleName,systemId) values (%s, %s);"
values = (('角色4', 4), ('角色5', 5), ('角色6', 6))
value = ('角色4', 4)
# 单条插入
# print mysql.insertOne(insertSql, value)
# 多条插入
# print mysql.insertMany(insertSql, values)


'''查询'''
sqlAll = "select id,roleName,systemId from t_role;"

# 查询表所有数据
result = mysql.getAll(sqlAll)
if result:
    for row in result:
        print "%s\t%s\t%s" % (row["id"], row["roleName"], row["systemId"])

# 查询指定条数数据
# result = mysql.getMany(sqlAll, 4)
# if result:
#   for row in result:
#       print "%s\t%s\t%s" % (row["id"], row["roleName"], row["systemId"])

# 查询第一条数据
# result = mysql.getOne(sqlAll)
# print "%s\t%s\t%s" % (result["id"], result["roleName"], result["systemId"])

'''修改'''
updateSql = "update t_position set postName='总经理' where id in (1,2);"
# print mysql.update(updateSql)

'''删除'''
deleteSQl = "DELETE  FROM t_role WHERE  id in (1);"
# print mysql.delete(deleteSQl)

# 释放资源
mysql.dispose()
