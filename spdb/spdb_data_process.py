import json

data = open('spdb_data.json').read()
json_data = json.loads(data)
# print(json_data)
for i in json_data:
    print(i)
