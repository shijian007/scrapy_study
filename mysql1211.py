#--coding = 'utf-8' --
import pymysql.cursors

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'100800112',
          'database':'learndb',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.Cursor,
          }

# 连接数据库
connection = pymysql.connect(**config)


try:
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM commodity WHERE price > 100 ORDER BY price'
        count = cursor.execute(sql) # 影响的行数
        print(count)
        result = cursor.fetchall()  # 取出所有行

        for i in result:            # 打印结果
            print(i)
        connection.commit()         # 提交事务
except:
    connection.rollback()           # 若出错了，则回滚

finally:
    connection.close()