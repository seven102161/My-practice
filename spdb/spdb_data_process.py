import json

data = open('spdb_data_original.json').read()
json_data = json.loads(data)
product_list = []
for i in json_data[0]['rows']:
    product_list.append(i)

with open('spdb_data.json', 'w', encoding='utf-8') as p:
    json.dump(product_list, p)
