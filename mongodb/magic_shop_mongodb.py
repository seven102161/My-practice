import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# # check connection
# print(client.stats)

# # show dbs
# print(client.list_database_names())

db = client['magic_shop']

# print(my_db.list_collection_names())

col_food = db['foods']
# print(data.count_documents({}))


# # drop collection
# col_food.drop()


# # 插入一行
# food_info = { "name": "Peter", "address": "Lowstreet 27" }
#
# x = col_food.insert_one(food_info)
# print(x.inserted_id)


# 插入多行
# food_infos = [
#     {"name": "美味饺子", "price": "15元/笼", "grade": "***"},
#     {"name": "章鱼饭", "price": "15元/碗", "grade": "****"},
#     {"name": "四层奶油蛋糕", "price": "10元/块", "grade": "*****"},
#     {"name": "新式甜甜圈", "price": "15元/个", "grade": "*****"},
#     {"name": "招牌雪糕", "price": "20元/只", "grade": "*****"},
#     {"name": "巨型芒果", "price": "15元/只", "grade": "**"},
#     {"name": "小小樱桃", "price": "5元/只", "grade": "***", "notes": "两只起卖"},
#     {"name": "玫瑰花茶", "price": "10元/壶", "grade": "****", "notes": "无限提供"},
#     {"name": "空心水饺", "price": "10元/个", "grade": "***"},
#     {"name": "魔法小药丸", "price": "5元/粒", "grade": "***"},
#     {"name": "奇妙奥利奥", "price": "10元/块", "grade": "*****"},
#     {"name": "香甜葡萄", "price": "10元/串", "grade": "***"},
# ]
#
# x = col_food.insert_many(food_infos)
# print(x.inserted_ids)

# # 查看一条(find_one())
# print(col_food.find_one())

# # 查看全部(find all ====== SELECT *)
# for i in col_food.find():
#     print(i)

my_query = {

}
my_view = {
    "_id": 0
}

for i in col_food.find(my_query, my_view).sort("grade", -1):
    print(i)
