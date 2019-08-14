"""
    写操作
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="stu",
                     charset="utf8")

# 创建游标对象(操作数据库语句，获取查询结果)
cur = db.cursor()

# 数据库操作
try:
    # 具体操作
    # 插入操作
    # name = input("name:")
    # age = input("age:")
    # sex = input("sex:")
    # score = input("score:")
    # sql = "insert into class_1 (name,age,sex,score) \
    # values ('%s',%s,'%s',%s)" % (name, age, sex, score)
    # sql = "insert into class_1 (name,age,sex,score) \
    #     values (%s,%s,%s,%s)"
    # cur.execute(sql, [name, age, sex, score])
    # 修改操作
    # sql = "update interest set price=10001 where name='ljh'"
    # cur.execute(sql)
    # 删除操作
    sql = "delete from class_1 where score<80"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()  # 如果提交异常，则回到提交前的状态
    print(e)

# 关闭游标和数据库(先关游标，再关数据库)
cur.close()
db.close()
