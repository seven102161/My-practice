import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="seven",
    password="Python0804",
    database="magic_shop"
)
cursor = cnx.cursor()

cursor.execute("DROP TABLE IF EXISTS foods")
cursor.execute("CREATE TABLE IF NOT EXISTS foods ("
               "food_id INT AUTO_INCREMENT PRIMARY KEY,"
               "name    VARCHAR(255) NOT NULL,"
               "price   DECIMAL(4,2) NOT NULL,"
               "unit    VARCHAR(45) NOT NULL,"
               "grade   VARCHAR(45),"
               "note    VARCHAR(255))")

sql = "INSERT INTO foods (name, price, unit, grade, note) " \
      "VALUES (%s, %s, %s, %s, %s)"
val = [
    ('美味饺子', 15, '元/笼', '***', ''),
    ('章鱼饭', 15, '元/碗', '****', ''),
    ('四层奶油蛋糕', 10, '元/块', '*****', ''),
    ('新式甜甜圈', 15, '元/笼', '****', ''),
    ('招牌雪糕', 20, '元/只', '*****', ''),
    ('巨型芒果', 15, '元/只', '**', ''),
    ('小小樱桃', 5, '元/只', '***', '两只起卖'),
    ('玫瑰花茶', 10, '元/壶', '****', '无限提供'),
    ('空心水饺', 10, '元/个', '***', ''),
    ('魔法小药丸', 5, '元/粒', '***', ''),
    ('奇妙奥利奥', 10, '元/块', '*****', ''),
    ('香甜葡萄', 10, '元/串', '***', '')
]

cursor.executemany(sql, val)

cnx.commit()

cursor.close()
cnx.close()
