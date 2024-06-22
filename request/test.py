import  pymongo
import  mysql
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myClient['test']
currency = my_db['currencies']
currencies = mysql.select()
if __name__ == '__main__':
  for data in currencies:
     print(data)
     x = currency.insert_one(data)
     print('插入成功！', x.inserted_id)


