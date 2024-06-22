import pymysql

con_test = pymysql.connect(user='root', password='123456', host='192.168.31.110', port=3306, db='chinesetests', charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
cursor = con_test.cursor()
query = "select * from score where name ='TOKKABULOV ARMAN'"
cursor.execute(query)
result = cursor.fetchone()
if __name__ == '__main__':
    print(result)
