import json
import pandas as pd


data = open('cmb_data.json').read()
json_data = json.loads(data)
df = pd.DataFrame(data=json_data, index=[i+1 for i in range(len(json_data))])

# df.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 2532 entries, 1 to 2532
Data columns (total 17 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   PrdCode          2532 non-null   object
 1   PrdName          2532 non-null   object
 2   TypeCode         2532 non-null   object
 3   Currency         2532 non-null   object
 4   BeginDate        2532 non-null   object
 5   EndDate          2532 non-null   object
 6   ExpireDate       2532 non-null   object
 7   Status           2532 non-null   object
 8   Term             2532 non-null   object
 9   Style            2532 non-null   object
 10  InitMoney        2532 non-null   object
 11  IncresingMoney   2532 non-null   object
 12  Risk             2532 non-null   object
 13  FinDate          2532 non-null   object
 14  SaleChannel      2532 non-null   object
 15  SaleChannelName  2532 non-null   object
 16  interest         2532 non-null   object
dtypes: object(17)
memory usage: 356.1+ KB
'''

print(df['Style'].describe())
print(df['Style'].unique())

print(df.loc[df['Style'] == '基金计划,固定收益型', ['PrdName','interest']])
print(df.loc[df['Style'] == '打新股,固定收益型', ['PrdName','interest']])