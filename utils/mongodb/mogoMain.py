#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 0. 安装 sudo pip install pymongo

# 1. 导入模块
from pymongo import *

# 2. 创建客户端对象
client = MongoClient(host='127.0.0.1',port=27017)

# 3. 获取数据库对象
db = client.wyh_ind

# 4. 对数据库对象进行操作

# 4.1 增
# db.pythoncoll.insert(
#     {
#         "name":"hello"
#     }
# )


# 4.2 更新
# 整体更新
# db.stu.update(
#     # 更新条件
#     {
#         "hometown":"蒙古"
#     },
#     # 更新内容
#     {
#         "name":"传智播客"
#     }
# )
# 局部更新
# db.stu.update(
#     # 更新条件
#     {
#         "hometown":"桃花岛"
#     },
#     # 更新内容
#     {
#         "$set":{
#             "name":"python"
#         }
#     }
# )
# 批量更新
# db.stu.update(
#     # 更新条件
#     {
#         "hometown":"大理"
#     },
#     # 更新内容
#     {
#         "$set":{
#             "name":"黑马程序员"
#         }
#     },
#     # 更新方式,使用关键词参数
#     multi=True
# )

# 4.3 查询
'''
为什么要使用游标
让使用内存更少
'''
# 返回是游标对象
cursor = db.user.find(
    # 查询条件
    {
    }
)
for row in cursor:
    print(row)
print(cursor)



# 4.4 删除
# db.stu.remove(
#     # 删除条件
#     {
#         "age":{"$gt":20}
#     }
# )
# 清空数据
# db.stu.remove({})