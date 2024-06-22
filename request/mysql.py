import pymysql


def select():
    host = '192.168.31.110'
    username = 'root'
    dbname = 'currency_rate'
    charset = 'utf8mb4'
    con = pymysql.connect(host=host, charset=charset, password='123456',
                      port=3306, user=username, db=dbname,
                      cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    query = "select * from currency where language_code = 'zh'"
    cursor.execute(query)
    return cursor
if __name__ == '__main__':
    for x in select():
        print(x)
